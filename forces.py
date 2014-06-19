from sys import argv

the_file = open('../forces/'+argv[1]+'.juj','r')

bins = range(10,540,5)
bucket = [[] for i in range(len(bins))]

X,F = [],[]
for line in the_file.readlines():
    rLine = line.split(' ')
    while '' in rLine: rLine.remove('')
    X += [float(rLine[1])]
    F += [float(rLine[3])]

itr = 0
for x in X:
    i = 0
    while x > bins[i]: i+= 1
    bucket[i] += [F[itr]]
    itr += 1

for b in range(len(bucket)):
	if len(bucket[b]) != 0: F[b] = sum(bucket[b])*1./len(bucket[b])
	else: F[b] = 0.
	if b == 0: X[b] = bins[b]/2.
	else: X[b] = (bins[b] +bins[b-1])/2.

x = []
f = []
for b in range(len(bucket)):
	if len(bucket[b]) != 0:
		f += [ 1.*sum(bucket[b])/len(bucket[b])]
		if b == 0: x += [bins[b]/2.]
		else: x +=  [(bins[b] +bins[b-1])/2.]

import matplotlib.pyplot as pl
import matplotlib
print 'matplotlib.__version__=', matplotlib.__version__
pl.plot(x,f)
pl.xlim(0,400)
pl.ylim(-10,200)
pl.xlabel(r'extension ($\AA$)')
pl.ylabel('force (pN)')
pl.savefig('../plots/fe_'+argv[1]+'.png')
#pl.savefig('../plots/'+argv[1]+'_159.png')
pl.show()
