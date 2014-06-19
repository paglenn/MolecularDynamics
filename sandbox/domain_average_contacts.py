#compare_domain_distances .py
# compare nonbonded distances

infile = open('GO_3L64.param','r')
#outfile = open('GO_MOD.param','w')

found = False
contactsC = dict()
contactsN = dict()
for line in infile.readlines():
	if 'NBFIX' in line: found=True
	if len(line) < 3: found = False

	if found and not 'NBFIX' in line:
		line2 = str(line.splitlines()[0])
		line2 = line2.split(' ')
		while '' in line2: line2.remove('')

		firstContact = int(line2[0].lstrip('G'))
		secondContact = int(line2[1].lstrip('G'))

		intervalC = range(60,165)+ range(1,13)

		if firstContact in intervalC and secondContact in intervalC:
			if not firstContact in contactsC.keys():
				contactsC[firstContact] = 0
			if not secondContact in contactsC.keys():
				contactsC[secondContact] = 0
			contactsC[firstContact] += 1
			contactsC[secondContact] += 1

		intervalN = range(13,60)

		if firstContact in intervalN and secondContact in intervalN:
			if not firstContact in contactsN.keys():
				contactsN[firstContact] = 0
			if not secondContact in contactsN.keys():
				contactsN[secondContact] = 0
			contactsN[firstContact] += 1
			contactsN[secondContact] += 1

	else:
		#outfile.write(line)
		pass
print max(contactsC.values())
print max(contactsN.values())

print min(contactsC.values())
print min(contactsN.values())

print 'C domain average num contacts: ', sum(contactsC.values())/(1.*len(contactsC.values()))
print 'N domain average num contacts: ', sum(contactsN.values())/(1.*len(contactsN.values()))

