# compare_domain_minima.py

infile = open('GO_3L64.param','r')

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

		intervalC = range(60,165)+range(1,13)

		if firstContact in intervalC and secondContact in intervalC:
			energyC += [ float(line2[2]) ]

		intervalN = range(13,60)

		if firstContact in intervalN and secondContact in intervalN:
			energyN += [ float(line2[2]) ]

	else:
		pass
print 'C domain well depth: ', sum(energyC)
print 'N domain well depth: ', sum(energyN)

print 'C domain Tf: ', -sum(energyC)/len(intervalC) / 0.0054
print 'N domain Tf: ', -sum(energyN)/len(intervalN) / 0.0054
#print 'C domain average well depth: ', sum(energyC)/len(energyC)
#print 'N domain average well depth: ', sum(energyN)/len(energyN)

