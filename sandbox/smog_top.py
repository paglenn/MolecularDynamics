infile = open('3L64_CA_shadow.12224.pdb.top','r')

start = False
sum = [0,0]
for line in infile.readlines():

	if 'bonds' in line and start: start = False
	if start and not 'pairs' in line and not 'weights' in line:
		pairWeight = line.split()[3:5]
	#	print pairWeight
		if pairWeight != []:
			sum[0] += float(pairWeight[0])
			sum[1] += float(pairWeight[1])
	if '[ pairs ]' in line: start = True

print [ 1.*s/164 for s in sum]
