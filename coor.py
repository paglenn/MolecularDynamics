# Paul Glenn
# plot reaction coordinate
# usage: python coor.py <run_name>
import pylab as pl
import sys
run = sys.argv[1]

the_file = open('../analysis/'+ run +'/coor.dat','r')
ref_file = open('../analysis/coor.dat','r')
X = [] ; Xr = []
Y = [] ; Yr = []

# Process new result file
for line in the_file:
	line = line.split('\t')
	X.append(int(line[0].strip()))
	Y.append(float(line[1].strip()))

#Compare with end of TMD
Yt = Y[98:1101:100]
# Process iENM file
for line in ref_file:
	line = line.split('\t')
	Xr.append(int(line[0].strip()))
	Yr.append(float(line[1].strip()))

# Chosen frames from iENM
Yr = [Yr[0],Yr[1],Yr[2],Yr[3],Yr[5],Yr[8],Yr[11],Yr[15],Yr[19],Yr[25],Yr[33]]
X = range(1,12)
Xr = list(X)

fig = pl.figure(facecolor='w')
font = {'family': 'monospace', 'size' : 14}
pl.rc('font', **font)
fig.add_subplot(111)
pl.hlines(1,0,6.0,'k','dotted')
p2, = pl.plot(X,Yt,'bo')
p3, = pl.plot(X,Yr,'ko')
pl.legend([p3,p2],['iENM','TMD'],loc=4)

# Formatting
textOffset = 0.2
pl.xlabel('frame  (variable timestep)')
pl.ylabel('RC')
pl.title('Trajectory')
pl.ylim(-0.2,1.1)
pl.yticks([-0.2,0.2,0.4,0.6,0.8,1.0])
# End formatting
pl.savefig('../plots/'+ run +'/RC.png')

pl.show()
