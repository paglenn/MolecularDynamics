# Usage: python contacts.py [inputfile] [outputfile]
from sys import argv

filename = ''#'100ns'#/'#+argv[1]
simtype = "eef1"

outputName = simtype#+argv[1]
'''
contact_fileC = open('../'+simtype+'/trajectories/'+filename+'/contacts.16-61.C.dat','r')
contact_fileN = open('../'+simtype+'/trajectories/'+filename+'/contacts.16-61.N.dat','r')

###########################C - domain ####################################
i = 0
j = 0
num_traj = 40
bigTraj = num_traj*[list()]
littleTraj = []
for line in contact_fileC.readlines():
	newLine = line.split(' ')
	while '' in newLine: newLine.remove('')
	newLine = [string.strip() for string in newLine]

	if newLine[0] != '':
		littleTraj.append([float(newLine[1])] )
	if newLine[0] == '' :
		bigTraj[i] = littleTraj
		littleTraj = []
		i += 1

import numpy as np
n = max([len(traj) for traj in bigTraj])
ctr = 1
netTraj = np.zeros((n,1))
for traj in bigTraj:
	smallTraj = np.array(traj)
	if len(traj) == n:
		netTraj += smallTraj
		ctr += 1

netTraj /= ctr
C = netTraj

################################### N - domain #############################
i = 0
j = 0
bigTraj = num_traj*[list()]
littleTraj = []
for line in contact_fileN.readlines():
	newLine = line.split(' ')
	while '' in newLine: newLine.remove('')
	newLine = [string.strip() for string in newLine]

	if newLine[0] != '':
		littleTraj.append([float(newLine[1])] )
	if newLine[0] == '' :
		bigTraj[i] = littleTraj
		littleTraj = []
		i += 1

import numpy as np
n = max([len(traj) for traj in bigTraj])
ctr = 1
netTraj = np.zeros((n,1))
for traj in bigTraj:
	smallTraj = np.array(traj)
	if len(traj) == n:
		netTraj += smallTraj
		ctr += 1

netTraj /= ctr
N = netTraj

import pylab as pl
pl.plot(range(1,n+1),C,'g',label="16,61 C-domain")
pl.plot(range(1,n+1),N,'b',label="16,61 N-domain")
pl.xlabel('frame')
pl.ylabel('fraction of native contacts')

contact_fileC.close()
contact_fileN.close()
'''

num_traj = 40

contact_fileC = open('../'+simtype+'/trajectories/'+filename+'/contacts.16-159.C.dat','r')
contact_fileN = open('../'+simtype+'/trajectories/'+filename+'/contacts.16-159.N.dat','r')

###########################C - domain ####################################
i = 0
j = 0
bigTraj = num_traj*[list()]
littleTraj = []
for line in contact_fileC.readlines():
	newLine = line.split(' ')
	while '' in newLine: newLine.remove('')
	newLine = [string.strip() for string in newLine]

	if newLine[0] != '':
		littleTraj.append([float(newLine[1])] )
	if newLine[0] == '' :
		bigTraj[i] = littleTraj
		littleTraj = []
		i += 1

import numpy as np
n = max([len(traj) for traj in bigTraj])
ctr = 1
netTraj = np.zeros((n,1))
for traj in bigTraj:
	smallTraj = np.array(traj)
	if len(traj) == n:
		netTraj += smallTraj
		ctr += 1

netTraj /= ctr
C = netTraj

################################### N - domain #############################
i = 0
j = 0
bigTraj = num_traj*[list()]
littleTraj = []
for line in contact_fileN.readlines():
	newLine = line.split(' ')
	while '' in newLine: newLine.remove('')
	newLine = [string.strip() for string in newLine]

	if newLine[0] != '':
		littleTraj.append([float(newLine[1])] )
	if newLine[0] == '' :
		bigTraj[i] = littleTraj
		littleTraj = []
		i += 1

import numpy as np
n = max([len(traj) for traj in bigTraj])
ctr = 1
netTraj = np.zeros((n,1))
for traj in bigTraj:
	smallTraj = np.array(traj)
	if len(traj) == n:
		netTraj += smallTraj
		ctr += 1

netTraj /= ctr
N = netTraj

import pylab as pl
pl.plot(range(1,n+1),C,'r',label="16,159 C-domain")
pl.plot(range(1,n+1),N,'k',label="16,159 N-domain")
pl.legend()
m = 1 if len(argv) < 4 else argv[3]
if m != 1:
	pl.title(r'Native Contacts for WT$^*$T4L, m = %s'%(m))
else:
	pl.title(r'Native Contacts for WT$^*$T4L')

pl.savefig('../plots/native_contacts/%s.png'%(outputName))
pl.show()

contact_fileC.close()
contact_fileN.close()

