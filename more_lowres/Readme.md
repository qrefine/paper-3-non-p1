# Additional Low-res PDB entries 
Low resolution set chosen to have only standard residues, no alternate locations and represent variety of space groups

Documented model preparation:

1.      phenix.fetch_pdb --mtz 

2.      leave only one set of data (not true for 5o5i, need to do) 

3.      qr.finalise > xxxx_complete.pdb

4.     NOT re-refined with phenix!

5.     qr.refine xxxx_complete.pdb  mode=gtest two_buffers=1 g_scan="1 5 10 15 25 50" > sanity check + chose optimal cpu-time maxnum_residues_in_cluster=N   

6.     /Refine_Step03_MaxResN/ qr.refine xxxx_complete.pdb xxxx.mtz mode=refine maxnum_residues_in_cluster=N quantum.nproc=2 parallel.nproc=10 max_bond_rmsd=0.02  stpmax=0.2 gradient_only=true clustering=true use_convergence_test=true  opt_log=1 restraints=qm  engine_name=xtb > xxxx_xtb_refine_MaxResN.log   

7.      /Refine_Step03/ stpmax=0.3 xxxx_xtb_refine_MaxResN_Step03.log

8.      /Refine_Step05/ stpmax=0.5 xxxx_xtb_refine_MaxResN_Step05.log

9.      /Refine_MaxItRef200/  stpmax=0.3 max_iterations_refine=200 xxxx_xtb_refine_MaxResN_Step03_MaxItRef200.log

10.     RE-refined with phenix : phenix.refine xxxx_complete.pdb xxxx.mtz > xxxx_complete_refine_001.pdb

11.     /Refine_PhenixStart_/...MaxResN/..Step03/..Step05/..MaxItRef200 . The same set repeated starting WITH phenix.refine
        qr.refine  xxxx_complete_refine_001.pdb xxx_complete_refine_001.mtz 

## Notes

1.  3hqb refinemnt failed not finding weights, clear problems around disulfide bonds. The same for the RE-refined with phenix start, also with stpmax=0.2. RUN again with "save_clusters = True"

2.  2r30 finished with error: minimization failed: 2, At end of further refinement. RE-refinement with phenix start fix problem.

     1 Rw: 0.1923 Rf: 0.2470 Rf-Rw: 0.0547 rmsd(b):  0.1585 rws:  1.000 n_fev: 24
     
  File "/usr/local/phenix-dev-3409_qrefine_update/modules/qrefine/results.py", line 80, in choose_best
    rewescas = rewescas.select(s)
RuntimeError: scitbx Internal Error: /home/builder/slave/phenix-nightly-intel-linux-2_6-x86_64-centos6/modules/cctbx_project/scitbx/array_family/selections.h(44): SCITBX_ASSERT(flags.size() == self.size()) failure.

3. 5xsl refinement starting from 5xsl_complete.pdb - OK, starting from 5xsl_complete_refine_001.pdb finished with error: minimization failed: 2 At end of further refinement:
     1 Rw: 0.2829 Rf: 0.3331 Rf-Rw: 0.0502 rmsd(b):  0.2727 rws:  1.000 n_fev: 417
  File "/usr/local/phenix-dev-3409_qrefine_update/modules/qrefine/results.py", line 80, in choose_best
    rewescas = rewescas.select(s)
RuntimeError: scitbx Internal Error: /home/builder/slave/phenix-nightly-intel-linux-2_6-x86_64-centos6/modules/cctbx_project/scitbx/array_family/selections.h(44): SCITBX_ASSERT(flags.size() == self.size()) failure.
