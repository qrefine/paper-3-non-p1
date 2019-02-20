# paper-3-non-p1
Data storage for paper 3 (non-P1 space group)

5c11.mtz,5c11.pdb   ----from PDB database 

5c11_refine_001.mtz,5c11_refine_001.pdb  ----run PDB file through phenix.refine

5c11_refine_001_complete.pdb  ----run 5c11_refine_001.pdb through qr.finalise

5c11_refine_001_complete_modified.pdb  ----set occupancies of H to 0 in finalised model

5c11_standard* has 4WQ replaced with LYS

BTW - 5bmi is not a viable candidate due to the MTN radical. Please ignore!

manually corrected model for 5c11: 5c11_gf2-xtb/5c11_modified_noCYS12_HG.pdb

--------------------------------------------------------------------------------

4gif is a simpler alternative for the non-P1 paper found by Pavel. 

It is 2.8 A resolution, P_3_2_1 symmetry.

Original PDB is showing several clashscores which are removed fully by both xtb and Terachem qr.refine.

Short summary what have been done + results can be found in "4gif_for_paper3_symmetry"
