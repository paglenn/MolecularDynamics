# Paul Glenn
# coor.py <run_name>
# plot reaction coordinate
import pylab as pl
import sys
run = sys.argv[1]

fig = pl.figure(facecolor='w')
font = {'family': 'monospace', 'size' : 14}
pl.rc('font', **font)
fig.add_subplot(111)
pl.hlines(1,0,6.0,'k','dotted')
for itr in range(10):
	the_file = open('../analysis/finerTMD/'+ run +'/eq_coor'+ str(itr)+'.dat','r')
	X = [] ; Xr = []
	Y = [] ; Yr = []

	# Process equilibration files
	for line in the_file:
		line = line.split('\t')
		X.append(int(line[0].strip()))
		Y.append(float(line[1].strip()))

	X = X[0:999:100]
	Y = Y[0:999:100]


	#pl.plot(X,Y)
	pl.quiver(X[:-1],Y[:-1], X[1:]-X[:-1], Y[1:]-Y[:-1],scale_units='xy',angles='xy',scale=1,color=cm.cool(itr/10.,1))

# Formatting
textOffset = 0.2
pl.xlabel('frame  (variable timestep)')
pl.ylabel('RC')
pl.title('Trajectory')
pl.ylim(-0.2,1.1)
pl.yticks([-0.2,0.2,0.4,0.6,0.8,1.0])
# End formatting
pl.savefig('../plots/finerTMD/' + str(run) + '.png')

pl.show()
