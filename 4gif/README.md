# 4gif is a simpler alternative for the non-P1 paper found by Pavel.

It is 2.8 A resolution, P_3_2_1 symmetry.

Documented model preparation:

1.      phenix.fetch_pdb --mtz 4gif

2.      phenix.refine 4gif.{pdb,mtz} ordered_solvent=true ordered_solvent.low_res=3

3.      qr.finalise 4gif_refine_001.pdb

4.      phenix.pdbtools 4gif_refine_001_complete.pdb occupancies.set=0 modify.selection="element H"

Short results summary in 4gif_for_paper3_symmetry_OKdocumented

Original PDB is showing several clashscores which are removed fully by both xtb and Terachem qr.refine.

# In the paper we included results with max_bond_rmsd = 0.02, stpmax=0.2 Å and max_iterations_refine=50

 paper-3-non-p1/4gif/4gif_xtb_refine/pdb_MaxItRef50/4gif_refine_001_complete.pdb_modified_Pavel16March_refined.pdb 
 
 # Modified 4H2O 
 
is the folder with new refinements starting from model where water S4 has been rotated to NOT create Hydrogen Bondings with the carboxylic acid of a symmetry copy of Arg713 nor acid side-chain oxygen atom (OE2) of Glu718. It is done to have nicer highlight for Figure 3 of paper3.
