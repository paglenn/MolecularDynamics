#compare_domain_distances .py
# compare nonbonded distances

infile = open('GO_3L64.param','r')
#outfile = open('GO_MOD.param','w')

found = False
S = 0
for line in infile.readlines():
	if 'NBFIX' in line: found=True
	if len(line) < 3: found = False

	if found and not 'NBFIX' in line:
		line2 = str(line.splitlines()[0])
		line2 = line2.split(' ')
		while '' in line2: line2.remove('')

		firstContact = int(line2[0].lstrip('G'))
		secondContact = int(line2[1].lstrip('G'))

		S += float(line2[2])
	else:
		#outfile.write(line)
		pass

print "Energy sum: ", S
