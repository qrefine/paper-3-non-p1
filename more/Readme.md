# Additional PDB entries 
chosen to have only standard residues, no alternate locations and represent variety of space groups: 5zkt, 6agy, 6jqs, 6n1l, 6ney, 6nfs, 6njg.


Documented model preparation:

1.      phenix.fetch_pdb --mtz 

2.      leave only one set of data  

3.      qr.finalise > xxxx_complete.pdb

4.     phenix.refine xxxx_complete.pdb xxxx.mtz

5.     qr.refine xxxx_complete_refine_001.pdb  mode=gtest two_buffers=1 g_scan="1 5 10 15 25 50" > sanity check + chose optimal cpu-time maxnum_residues_in_cluster=N   

6.     /Refine_MaxResN/ qr.refine xxxx_complete_refine_001.pdb xxxx_complete_refine_001.mtz mode=refine maxnum_residues_in_cluster=N quantum.nproc=2 parallel.nproc=10 max_bond_rmsd=0.02  stpmax=0.2 gradient_only=true clustering=true use_convergence_test=true  opt_log=1 restraints=qm  engine_name=xtb  > xxxx_xtb_refine_MaxResN.log   

7.      /Refine_Step03/ stpmax=0.3 xxxx_xtb_refine_MaxResN_Step03.log

8.      /Refine_Step05/ stpmax=0.5 xxxx_xtb_refine_MaxResN_Step05.log

9.      /Refine_MaxItRef200/  stpmax=0.3 max_iterations_refine=200 xxxx_xtb_refine_MaxResN_Step03_MaxItRef200.log

#Notes

1.  6n1l: stpmax=0.3 and 0.5 "lost" good weights 

2.  6njg: stpmax=0.5 minimization failed

