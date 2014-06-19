# Paul Glenn
# plotResRMSD.py
# for plotting rmsd by residue
# python plotResRMSD.py <run name>
import pylab as pl
import sys

run = sys.argv[1]
pl.figure(edgecolor='w')
the_file = open('../analysis/' + run + '/residue_rmsd.dat','r')
X = []
Y = []
for line in the_file:
	line = line.split('\t')
	X.append(int(line[0].strip()))
	Y.append(float(line[1].strip()))


AX = pl.plot(X,Y,'k.')

# Formatting
textOffset = 0.1
pl.plot(X[29:66],Y[29:66],'m.')
pl.plot(X[117:166],Y[117:166],'r.')
pl.xlabel('residue no.')
pl.ylabel(r'RMSD ($\AA$)')
pl.xlim(1,214)
pl.text(X[Y.index(max(Y[29:66]))],max(Y[29:66])+textOffset,'NMP')
pl.text(X[Y.index(max(Y[117:166]))],max(Y[117:166])+textOffset,'LID')
pl.xticks(range(0,215,45)+[118,167]+ [30,67])
# End formatting

pl.show()
pl.savefig('../plots/' + run + '/res_rmsd.png')
