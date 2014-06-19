from sys import argv

mT = '87'

num_traj = 25

contact_fileC = open('../Go_trajectories/p87/multiplot_16-61_C.dat','r')
contact_fileN = open('../Go_trajectories/p87/multiplot_16-61_N.dat','r')
#contact_fileC = open('../Go_trajectories/p%s/multiplot_16-61_C.dat'%(mT),'r')
#contact_fileN = open('../Go_trajectories/p%s/multiplot_16-61_N.dat'%(mT),'r')

m = float(mT.strip('m'))
m = m/100. if m > 10 else m/10.

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
pl.plot(range(1,n+1),C,'g',label="C-domain 16,61")
pl.plot(range(1,n+1),N,'b',label="N-domain 16,61")
pl.xlabel('frame')
#pl.legend()
pl.ylabel('fraction of native contacts')
#pl.title('m = %s for 16,61 WT*T4L'%(m))

#pl.savefig('../plots/native_contacts_16-61_%s.png'%(m))

contact_fileC.close()
contact_fileN.close()

mT = '87'

num_traj = 25

contact_fileC = open('../Go_trajectories/WT/multiplot_16-159_C.dat','r')
contact_fileN = open('../Go_trajectories/WT/multiplot_16-159_N.dat','r')
#contact_fileC = open('../Go_trajectories/p%s/multiplot_16-159_C.dat'%(mT),'r')
#contact_fileN = open('../Go_trajectories/p%s/multiplot_16-159_N.dat'%(mT),'r')

m = float(mT.strip('m'))
m = m/100. if m > 10 else m/10.

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
pl.plot(range(1,n+1),C,'c',label="C-domain, 16,159")
pl.plot(range(1,n+1),N,'k',label="N-domaini, 16,159")
pl.legend()
#pl.xlabel('frame')
#pl.ylabel('fraction of native contacts')
pl.title('m = %s for WT*T4L'%(m))

#pl.savefig('../plots/native_contacts_16-159_%s.png'%(m))
pl.savefig('../plots/native_contacts_%s.png'%(m))
pl.show()

contact_fileC.close()
contact_fileN.close()

