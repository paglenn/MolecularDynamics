#residues="16-61"
residues="16-159"
#residues="1-164"
type="WT"
#type="CP"
modifier="p89"
num="0.89"
#filename="smd.".residues."_RG"
#set output "../analysis/".filename.".ps"
set output "../plots/".residues."_GO_".type."_".modifier.".ps"
set terminal postscript color solid 
set terminal postscript enhanced "Helvetica" 20
set ylabel "Radius of gyration (relative to native state)"
set xlabel "frame"
set title residues." ".type."-T4L"." ".num."*NBEnergy"
set grid 
set style data points
set key left top

#filename="Go.".residues."_2_RG"
#C_file = "../analysis/".type."/".filename."_C.txt"  
#N_file = "../analysis/".type."/".filename."_N.txt" 
do for [t=1:10] {
	filename="Go.".residues."_".t."_RG"
	set title residues." ".type."-T4L"." ".num."*NBEnergy, frame ".t
	C_file = "../analysis/".type."/".filename."_C.txt"  
	N_file = "../analysis/".type."/".filename."_N.txt" 
	plot N_file title "N-domain" pointtype 7, C_file title "C-domain" pointtype 7
}


