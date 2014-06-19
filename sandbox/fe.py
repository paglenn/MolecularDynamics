# Single pull group analysis file for gromacs

num_traj = 1
forceFiles = []
posFiles = []
for x in range(1,num_traj+1):
    forceFiles.append(open('pullf.xvg','r'))
    posFiles.append(open('pullx.xvg','r'))

forceLines = [file.readlines() for file in forceFiles ]
posLines = [file.readlines() for file in posFiles ]


F = []
X  = []
for i in range(num_traj):
	for fLine, pLine in zip(forceLines[i],posLines[i]):
		fLine = fLine.strip()
		fLine = fLine.split('\t')
		F.append(float(fLine[1])+ float(fLine[2])) # finished processing forces
		pLine = pLine.strip()
		pLine = pLine.split('\t')
		z1,z2 = [float(k) for k in [pLine[2],pLine[3]] ];from math import fabs
		r = fabs(z1) + fabs(z2)
		X.append(r) # distances in nm

# rescale forces to Angstrom relative to original positon
X = [10*(x-X[0]) for x in X]

#Binning
binSize = 5
bins = range(int( min(X) ),int( max(X) + 2*binSize), binSize)
buckets = [ []  for i in range(len(bins)) ]
x = []
f = []

itr = 0
for x in X:
	i=0
	while x > bins[i]:
		#print x, bins[i]
		i+= 1
	buckets[i].append(F[itr])
	itr += 1

X = [ 0 for x in buckets]
F = list(X)
for b in range(len(buckets)):
	# average the forces in each bucket
	if len(buckets[b]) != 0: F[b] = sum(buckets[b])*1./len(buckets[b])
	else:F[b] = 0.
	if b == 0 : X[b] = bins[b]/2.
	else: X[b] = (bins[b] + bins[b-1])/2.

title = ''' @    title "Force-extension"          \n'''
xaxis = ''' @    xaxis  label "Extension (nm)"    \n'''
yaxis = ''' @    yaxis  label "Force (kJ/mol/nm)" \n'''
world = ''' @    world -1, 0, 300, 100			  \n'''
type  = ''' @TYPE xy                              \n'''
outfile = open('force_ext.xvg','w')

outfile.write(title)
outfile.write(xaxis)
outfile.write(yaxis)
outfile.write(world)
outfile.write(type)
for i in range(len(X)):
    outfile.write( str(X[i]) + '\t' +str(F[i])+ '\n' )
outfile.close()
