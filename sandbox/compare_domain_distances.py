#compare_domain_distances .py
# compare nonbonded distances

infile = open('GO_3L64.param','r')
#outfile = open('GO_MOD.param','w')

found = False
energyC = list()
energyN = list()
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

		if firstContact in intervalC and secondContact in intervalC:
			energyC += [ float(line2[3]) ]
			if abs(firstContact - secondContact) == 1: print 'BANG'

		intervalN = range(13,59)

		if firstContact in intervalN and secondContact in intervalN:
			energyN += [ float(line2[3]) ]
			if abs(firstContact - secondContact) == 1: print 'BANG'

	else:
		#outfile.write(line)
		pass

print 'C domain average contact distance: ', sum(energyC)/len(energyC)
print 'N domain average contact distance: ', sum(energyN)/len(energyN)

