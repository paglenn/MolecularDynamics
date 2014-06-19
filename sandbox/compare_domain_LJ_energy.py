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
			energyC += [ LJ(float(line2[3])) ]
			distanceC += [float(line2[3])]

		elif firstContact in intervalN and secondContact in intervalN:
			energyN += [ LJ(float(line2[3])) ]
			distanceN += [float(line2[3])]


	else:
		pass

print 'C domain average: ' , sum(energyC)/len(energyC)
print 'N domain average: ' , sum(energyN)/len(energyN)

import pylab as pl
pl.plot(distanceN, energyN, 'b.', label='N domain')
pl.plot(distanceC, energyC, 'g.', label='C domain')
pl.legend()
pl.show()
