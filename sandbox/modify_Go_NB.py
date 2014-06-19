# modify_Go_NB.py
# modify Go model Non Bonded contacts

infile = open('GO_3L64.param','r')
outfile = open('GO_MOD.param','w')

found = False
for line in infile.readlines():
	if 'NBFIX' in line: found=True
	if len(line) < 3: found = False

	if found and not 'NBFIX' in line:
		line2 = str(line.splitlines()[0])
		line2 = line2.split(' ')
		while '' in line2: line2.remove('')

		firstContact = int(line2[0].lstrip('G'))
		secondContact = int(line2[1].lstrip('G'))

		interval = range(60,165)

		if firstContact in interval and secondContact in interval:
			line2[2] = str( round(0.7*float(line2[2]),6) )
			print firstContact, secondContact

		# reformat
		line2[0]= '{0:{width}}'.format(line2[0],width=4)
		line2[1]= '{0:{width}}'.format(line2[1],width=4)
		line2[2]= '{0:{width}}'.format(line2[2],width=9)
		line2[3]= '{0:{width}}'.format(line2[3],width=8)
		newLine = line2[0]+'    '+line2[1]+'       '+line2[2]+'    '+line2[3]
		outfile.write(newLine+'\n')

	else:
		outfile.write(line)
		pass
