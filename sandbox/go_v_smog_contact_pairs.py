go = open('go_contacts.txt','r')
smog = open('3L64_CA_shadow.12224.pdb.contacts','r')
#smog = open('3L64_CA_shadow_4.5.12397.pdb.contacts','r')
smog_total = 457
go_total = 408
smog_4p5_total = 354

C_domain = range(1,13) + range(60,165) # 1-12, 60-164
N_domain = range(13,60) #13-59
g_X = [] ; g_Y = []
s_X = [] ; s_Y = []
for line in go.readlines():
	line2 = line.split()
	line2[0] = line2[0].replace('G','')
	line2[1] = line2[1].replace('G','')
	pair = (int(line2[0]),int(line2[1]))
	g_X += [ pair[0] ]
	g_Y += [ pair[1] ]

gCC, gCN, gNN = [0,0,0]
for pair in zip(g_X,g_Y):
	if pair[0] in C_domain and pair[1] in C_domain:
		gCC += 1
	elif pair[0] in N_domain and pair[1] in N_domain:
		gNN += 1
	elif pair[0] in N_domain and pair[1] in C_domain:
		gCN += 1
	elif pair[0] in C_domain and pair[1] in N_domain:
		gCN += 1
print 'gCC ', gCC
print 'gCN ', gCN
print 'gNN ', gNN
print 'checksum: ',gCC +gNN +gCN == go_total
for line in smog.readlines():
	line2 = line.split()
	pair = (int(line2[1]),int( line2[3]) )
	s_X += [ pair[0] ]
	s_Y += [ pair[1] ]

sCC, sCN, sNN = [0,0,0]
for pair in zip(s_X,s_Y):
	if pair[0] in C_domain and pair[1] in C_domain:
		sCC += 1
	elif pair[0] in N_domain and pair[1] in N_domain:
		sNN += 1
	elif pair[0] in N_domain and pair[1] in C_domain:
		sCN += 1
	elif pair[0] in C_domain and pair[1] in N_domain:
		sCN += 1
print 'sCC ', sCC
print 'sCN ', sCN
print 'sNN ', sNN
print 'checksum: ',sCC +sNN +sCN == smog_total

from pylab import *
subplot(2,1,1)
plot(s_X,s_Y,'bo',label='SMOG - 457')
ylabel('residue 2 index')
#plot(s_X,s_Y,'bo',label='SMOG - 354')
legend(framealpha=0.5,loc=4)
subplot(2,1,2)
plot(g_X,g_Y,'ro',label='GO - 408')
xlabel('residue 1 index')
ylabel('residue 2 index')
legend(framealpha=0.5,loc=4)
savefig('../plots/go_vs_smog_contacts.png')
show()
