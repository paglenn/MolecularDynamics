# Paul Glenn
# relative_coor.py
# for plotting rc for two domains in a parametric form.
import pylab as pl
import sys
fileList = ['AK_100_ion','AK_150_ion','AK_225_ion','AK_250_ion','AK_175_ion']
font = {'family': 'monospace', 'size' : 14}
pl.rc('font', **font)
pl.figure(facecolor='w')
for i in fileList:
#pl.figure(1,edgecolor='w')
	run = i
	nmp_file = open('../analysis/'+ run + '/nmp.dat','r')
	lid_file = open('../analysis/'+ run +'/lid.dat','r')
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

#post - eq frames
	X1 = X[166:1000:166]
	Y1 = Y[166:1000:166]

# pre - eq frames
	X2 = X[83:1000:167]
	Y2 = Y[83:1000:167]

#iENM frames
	for nmpLine, lidLine in zip(ref_nmp,ref_lid):
		lidLine = lidLine.split('\t')
		nmpLine = nmpLine.split('\t')
		Xr.append(float(nmpLine[1].strip()))
		Yr.append(float(lidLine[1].strip()))

#iENM frames
	Xr = [Xr[0],Xr[1],Xr[4],Xr[10],Xr[20],Xr[33]]
	Yr = [Yr[0],Yr[1],Yr[4],Yr[10],Yr[20],Yr[33]]
'''
# Plot
	p1, = pl.plot(X1,Y1,'ro')
	p2, = pl.plot(X2,Y2,'bo')
	p3, = pl.plot(Xr,Yr,'ko')
	pl.legend([p3,p2,p1],['iENM','TMD','TMD+eq'],loc=4)
'''
# Formatting
	pl.vlines(1,-0.2,1.0,'k','dotted')
	pl.hlines(1,-0.2,1.0,'k','dotted')
	pl.yticks([-0.1,0.2,0.4,0.6,0.8,1.0,1.1])
	pl.xticks([-0.1,0.2,0.4,0.6,0.8,1.0,1.1])
	pl.xlabel('NMP RC')
	pl.ylabel('LID RC')
	pl.title('LID and NMP domains')
# End formatting
	pl.savefig('../plots/'+ run +'/lidvnmp.png')

pl.show()
