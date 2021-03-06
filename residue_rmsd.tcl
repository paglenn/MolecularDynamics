# % $Id: residue_rmsd.tcl,v 1.4 2006/03/06 23:56:46 timisgro Exp $
#
set ccr 1
set run_name AK
global target_dir
if {$ccr} {
	mol new ../results/end_dry.pdb
	set target_dir "../analysis/"
} else {
	mol new ../results/$run_name/end_dry.pdb 
	set target_dir "../analysis/$run_name"
}
proc rmsd_residue_over_time {{mol top} res} {
    global target_dir
	
	#set target_dir ../analysis/
    # use frame 0 for the reference
    set reference [atomselect $mol "protein and alpha" frame 0]
    # the frame being compared
    set compare [atomselect $mol "protein and alpha"]
    #make a selection with all atoms
    set all [atomselect top all]
    #get the number of frames
    set num_steps [molinfo $mol get numframes]
    #open file for writing
    set fil [open ${target_dir}/residue_rmsd.dat w]
    
    foreach r $res {
	set rmsd($r) 0
    }
    
    #loop over all frames in the trajectory
    for {set frame 0} {$frame < $num_steps} {incr frame} {
	puts "Calculating rmsd for frame $frame ..."
	# get the correct frame
	$compare frame $frame
        $all frame $frame
	# compute the transformation
	set trans_mat [measure fit $compare $reference]
	# do the alignment
	$all move $trans_mat
	
	# compute the RMSD
	#loop through all residues
	foreach r $res {
	    set ref [atomselect $mol "protein and resid $r and alpha" frame 0]
	    set comp [atomselect $mol "protein and resid $r and alpha" frame $frame]
	    set rmsd($r) [expr $rmsd($r) + [measure rmsd $comp $ref]]
	    $comp delete
	    $ref delete
	}
    }
    
    set ave 0
	foreach r $res {
	    set rmsd($r) [expr $rmsd($r)/$num_steps]
	    # print the RMSD
	    puts "RMSD of residue $r is $rmsd($r)"
	    puts $fil " $r \t $rmsd($r)"
	    set res_b [atomselect $mol "resid $r"] 
            $res_b set user $rmsd($r)
            $res_b delete
	    set ave [expr $ave + $rmsd($r)]
	}
	
    set ave [expr $ave/[llength $res]]
    puts " Average rmsd per residue:   $ave"
    close $fil
}

set sel_resid [[atomselect top "protein and alpha"] get resid]
rmsd_residue_over_time top $sel_resid
exit
