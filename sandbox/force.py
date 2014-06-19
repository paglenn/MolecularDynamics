# force_extension.py
# py force_extension.py [name]

from sys import argv
if len(argv) < 2:
	print 'Usage: py force_extension.py [dir_name]'
	quit()

dir_name= argv[1]
num_trajectories = 25

#resids = '16-61'
resids = '16-159'
#resids = '4-49'
infiles = list()
frameskip = 100
bins = range(10,510,10)
from numpy import empty
bucket = [[] for i in range(len(bins))]

#for i in range(1,num_trajectories+1):
#	infiles +=  [open('../forces/0401/%s/smd100.%s_%i.juj'%(dir_name,resids,i),'r') ]

infiles = [ open('../forces/0401/%s.juj'%(dir_name),'r') ]
allF = []
allExt = []
for file in infiles:

	force = list()
	extension = list()
	start = 0
	ctr = 0
	for line in file.readlines():
		if ctr % frameskip == 0:
			modLine =  line.splitlines()[0]
			modLine = modLine.split(' ')
			while '' in modLine: modLine.remove('')

			x = float(modLine[1])
			f = float(modLine[3])
			force += [ f ]
			extension += [ abs(x) ]

		ctr += 1
	# end loop over single trajectory

	allF.append(force)
	allExt.append(extension)
	# end loop over trajectories

# Binning
for i in range(len(allExt)):
	for j in range(len(allExt[i])):
		x = allExt[i][j]
		k = 0
		while x > bins[k]: k += 1
		(bucket[k]).append( allF[i][j] )

F = [[] for b in bucket]
X = list(F)

for b in range(len(bucket)):
	if len(bucket[b]) != 0: F[b] = sum(bucket[b])*1./len(bucket[b])
	else: F[b] = 0.
	if b == 0: X[b] = bins[b]/2.
	else: X[b] = (bins[b] +bins[b-1])/2.

#print F
#print X

import pylab as pl
pl.plot(X,F)
pl.xlim(10,300)
pl.ylim(-10,60)
pl.grid(True)
pl.show()

###########################################
quit()
from collections import Counter
data = Counter( [ len(f) for f in allF] )
mode = data.most_common(1)[0][0]
redF = [ X for X in allF if len(X) == mode ]
redExt = [X for X in allExt if len(X) ==  mode ]

import numpy as np
F = np.average(np.array(redF),axis = 0 )
ext = np.average(np.array(redExt), axis = 0)/10.

import pylab as pl
for traj in range(num_trajectories):
	F = allF[traj]
	ext = allExt[traj]
	pl.plot(ext,F)

pl.xlabel('extension (nm)')
pl.ylabel('force (pN)')

pl.savefig('../plots/0401/force_extension_'+resids +'_'+ dir_name+ '.png')
pl.show()
