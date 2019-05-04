# Additional Low-res PDB entries 
Low resolution set chosen to have only standard residues, no alternate locations and represent variety of space groups

Documented model preparation:

1.      phenix.fetch_pdb --mtz 

2.      leave only one set of data  

3.      qr.finalise > xxxx_complete.pdb

4.     NOT re-refined with phenix!

5.     qr.refine xxxx_complete.pdb  mode=gtest two_buffers=1 g_scan="1 5 10 15 25 50" > sanity check + chose optimal cpu-time maxnum_residues_in_cluster=N   

6.     /Refine_Step03_MaxItRef200/ qr.refine xxxx_complete.pdb xxxx.mtz mode=refine maxnum_residues_in_cluster=N quantum.nproc=2 parallel.nproc=10 max_bond_rmsd=0.02  stpmax=0.3 gradient_only=true clustering=true use_convergence_test=true  opt_log=1 restraints=qm  engine_name=xtb max_iterations_refine=200 > xxxx_xtb_refine_Step03_MaxItRef200.log   


## Notes


