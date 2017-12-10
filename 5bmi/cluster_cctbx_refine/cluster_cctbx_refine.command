

@ to debug qm refinement, same parameters for qm refinement, except restraints=cctbx
qr.refine ../5bmi/5bmi_refine_001.mtz ../5bmi/5bmi_refine_001_complete.pdb_modified.pdb  restraints=cctbx clustering=true  mode=refine maxnum_residues_in_cluster=10 stpmax=0.5 max_iterations=50   number_of_macro_cycles=1 two_buffers=false charge_embedding=true  charge_cutoff=5 restraints_weight_scale=8.0 nproc=40 > cluster_cctbx_refine.log 2>&1 &
