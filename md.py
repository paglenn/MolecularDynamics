# Paul Glenn
# md.py
# Geometric analysis script
import MDAnalysis as md
import MDAnalysis.analysis
from sys import argv # Hold command line input
from numpy import shape

def RC(res_file, begin, end):
	'''RC(post-md file, beginning structure, final structure)'''
	result = md.Universe(psf, res_file)

	#rCA -- result CA carbon
	#bCA -- beginning structure CA
	#eCA -- end
	rCA = result.selectAtoms("name CA") # KALP == protein
	bCA = md.Universe(begin).selectAtoms("name CA")
	eCA = md.Universe(begin).selectAtoms("name CA")

	#print result.trajectory; quit()
	#for frame in result.trajectory:
		#rCA = frame.selectAtoms("name CA") # KALP == protein
		#print shape(frame)


psf = '../protein/ak_open.psf'
res_file = '../results/TMDk300/end_dry.dcd'
begin = '../protein/4AKE.pdb'
end = '../protein/1AKE.pdb'
RC(res_file, begin, end)
