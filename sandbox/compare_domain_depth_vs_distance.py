# calculate domain energy based on distances in Go param file for NB contacts

infile = open('GO_3L64.param','r')

found = False
energyC = list()
distanceC = list()
energyN = list()
distanceN = list()
LJ = lambda r: 13./r**12 - 18./r**10 + 4./r**6
for line in infile.readlines():
	if 'NBFIX' in line: found=True
	if len(line) < 3: found = False

	if found and not 'NBFIX' in line:
		line2 = str(line.splitlines()[0])
		line2 = line2.split(' ')
		while '' in line2: line2.remove('')

		firstContact = int(line2[0].lstrip('G'))
		secondContact = int(line2[1].lstrip('G'))

		intervalC = range(60,165)
		intervalN = range(13,60)

		if firstContact in intervalC and secondContact in intervalC:
			energyC += [ float(line2[2]) ]
			distanceC += [float(line2[3])]

		elif firstContact in intervalN and secondContact in intervalN:
			energyN += [ float(line2[2]) ]
			distanceN += [float(line2[3])]


	else:
		pass

print 'C domain average: ' , sum(energyC)/len(energyC)
print 'N domain average: ' , sum(energyN)/len(energyN)

import pylab as pl
pl.plot(distanceN, energyN, 'bo', label='N domain')
pl.plot(distanceC, energyC, 'go', label='C domain')
pl.legend()
pl.title(r'$G\bar{o}$ LJ-well depth distribution vs domain')
pl.xlabel(r'contact distance $r_{ij}$')
pl.ylabel(r'potential well depth $\epsilon_{ij}$')
pl.text(6,-1.7, r'$u_{LJ,G\bar{o}} = \epsilon_{ij}[13(\frac{r_{eq}}{r_{ij}})^{12} - 18(\frac{r_{eq}}{r_{ij}})^{10} + 4(\frac{r_{eq}}{r_{ij}})^6]$', size='x-large')
pl.savefig('../plots/GoModel_NB_contact_depth_distribution')
pl.show()
