# Paul Glenn
# relative_coor.py
# for plotting rc for two domains in a parametric form.
import pylab as pl
import sys
from numpy import array
import matplotlib.cm as cm
fileList = ['02','03','26','34']
font = {'family': 'monospace', 'size' : 14}
pl.rc('font', **font)
pl.figure(facecolor='w')

for i in fileList:
#pl.figure(1,edgecolor='w')
	run = i
	for itr in range(10):
		nmp_file = open('../analysis/finerTMD/nmp'+ run + '/eq_coor' + str(itr)+'.dat','r')
		lid_file = open('../analysis/finerTMD/lid'+ run + '/eq_coor' + str(itr)+'.dat','r')
		ref_nmp = open('../analysis/nmp.dat','r')
		ref_lid = open('../analysis/lid.dat','r')
		X = []; Xr = []
		Y = []; Yr = []

	#TMD frames
		for nmpLine, lidLine in zip(nmp_file,lid_file):
			lidLine = lidLine.split('\t')
			nmpLine = nmpLine.split('\t')
			X.append(float(nmpLine[1].strip()))
			Y.append(float(lidLine[1].strip()))
		X = array(X)
		Y = array(Y)
		#print X, Y ; quit()
		#pl.plot(X,Y)
		pl.quiver(X[:-1],Y[:-1], X[1:]-X[:-1], Y[1:]-Y[:-1],scale_units='xy',angles='xy',scale=1,color=cm.cool(itr/10.,1))
		#pl.show()
		#quit()

#iENM frames
	for nmpLine, lidLine in zip(ref_nmp,ref_lid):
		lidLine = lidLine.split('\t')
		nmpLine = nmpLine.split('\t')
		Xr.append(float(nmpLine[1].strip()))
		Yr.append(float(lidLine[1].strip()))

#iENM frames
	Xr = [Xr[0],Xr[1],Xr[2],Xr[3],Xr[5],Xr[8],Xr[11],Xr[15],Xr[19],Xr[27],Xr[33]]
	Yr = [Yr[0],Yr[1],Yr[2],Yr[3],Yr[5],Yr[8],Yr[11],Yr[15],Yr[19],Yr[27],Yr[33]]
# Plot
	pl.plot(Xr,Yr,'ko')

# Formatting
	pl.vlines(1,-0.2,1.0,'k','dotted')
	pl.hlines(1,-0.2,1.0,'k','dotted')
	pl.yticks([0,0.2,0.4,0.6,0.8,1.0,1.1])
	pl.xticks([0,0.2,0.4,0.6,0.8,1.0,1.1])
	pl.xlim(0,1)
	pl.ylim(0,1)
	pl.xlabel('NMP RC')
	pl.ylabel('LID RC')
	pl.title('LID and NMP domains')
	pl.show()
# End formatting
	#pl.savefig('../plots/'+ run +'/lidvnmp' + run+'.png')

