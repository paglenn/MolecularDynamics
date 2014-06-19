from sys import argv

#Parameters
m = 0.9
if 0: resids = "16-61"
else: resids = "16-159"
if True: type = "WT"
else: type = "CP13"
num_trajectories = 10


Nfiles = []
Cfiles = []
for i in range(1,num_trajectories+1):
	Cfiles.append( open("../analysis/WT/Go.%s_%i_RG_C.txt"%(resids,i),'r') )
	Nfiles.append( open("../analysis/WT/Go.%s_%i_RG_N.txt"%(resids,i),'r') )


C = []
N = []
for (Nfile,Cfile) in zip(Nfiles,Cfiles):
	N.append(Nfile.readlines())
	C.append(Cfile.readlines())

numFrames = len(N[0])
import numpy as np
RG_C = np.zeros(numFrames)
RG_N = np.zeros(numFrames)
num_counted = 0

for i in range(num_trajectories):
	N[i] = [string.strip() for string in N[i]]
	C[i] = [string.strip() for string in C[i]]

	N[i] = [float(string) for string in N[i]]
	C[i] = [float(string) for string in C[i]]

	N[i] = np.array(N[i])
	print N[i].shape

	if np.size(N[i]) == numFrames:
		RG_C += C[i]
		RG_N += N[i]
		num_counted +=1

RG_C /= num_counted
RG_N /= num_counted

import pylab as pl
pl.plot(range(numFrames), RG_N,'b.',label=r'$\hat{R_{g}}$-N')
pl.plot(range(numFrames), RG_C,'g.',label=r'$\hat{R_{g}}$-C')
pl.legend(loc = 'lower right')
pl.title('%s Nonbonded energy modifier for %s %s*T4L'%(m,resids,type))

pl.savefig('../plots/'+resids+"_GO_WT_%s_avg.png"%(m))
pl.show()



#for (Nline, Cline) in zip(Nfile.readlines(),Cfile.readlines()):



