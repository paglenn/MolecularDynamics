from sys import argv
import os
#Parameters
outfile = argv[1]
num_trajectories = 10
#resids = "16-61"
resids = "16-159"
species = "WT"
#species = "CP13"
#method = "Go"
#method = "smog"
method = "eef1"
Nfiles = []
Cfiles = []
for i in range(0,num_trajectories):
	parameters = (species,method,resids,i)
	Cfiles.append(open("../analysis/%s/%s.%s_%i_RG_C.txt"%parameters,'r'))
	Nfiles.append(open("../analysis/%s/%s.%s_%i_RG_N.txt"%parameters,'r'))


C = []
N = []
for (Nfile,Cfile) in zip(Nfiles,Cfiles):
	N.append(Nfile.readlines())
	C.append(Cfile.readlines())

numFrames = max( [len(L) for L in N])
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
#pl.title('%s  * NBenergy :  %s %s*T4L'%(mod,resids,species))
#pl.xlim(0,105)
#pl.ylim(0.95,3)
pl.title('%s %s*T4L'%(resids, species))
pl.xlabel('frame')
pl.ylabel('Radius of gyration ( relative to native state)')

pl.savefig('../plots/gyration/'+outfile+".png")
pl.show()

#os.rmtree('../analysis/%s/'%(species))
#os.mkdir('../analysis/%s/'%(species))
#for (Nline, Cline) in zip(Nfile.readlines(),Cfile.readlines()):



