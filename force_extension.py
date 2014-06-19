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
frameskip = 200
infiles = list()

for i in range(1,num_trajectories+1):
	infiles +=  [open('../forces/0401/%s/smd100.%s_%i.juj'%(dir_name,resids,i),'r') ]

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

			force += [ float(modLine[3]) ]
			if start == 0: start = float(modLine[1])
			extension += [ float(modLine[2]) - start ]
		ctr += 1
	# end loop over single trajectory

	allF.append(force)
	allExt.append(extension)
	# end loop over trajectories
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
pl.xlim(

pl.savefig('../plots/0401/force_extension_'+resids +'_'+ dir_name+ '.png')
pl.show()
