#!/bin/sh
dirname=$1
pushd ~/Dropbox/MolecularDynamics/AdenylateKinase\[AK\]/scripts/

mkdir ../analysis/$dirname
scp -r paulglen@rush.ccr.buffalo.edu:/panasas/scratch/paulglen/$dirname/analysis/* ../analysis/$dirname/
#scp -r paul2@hangroup.physics.buffalo.edu:~/AdenylateKinase\[AK\]/analysis/$dirname ../analysis/

#scp -r paul2@hangroup.physics.buffalo.edu:~/AdenylateKinase\[AK\]/plots/$dirname/ ../plots/

popd
