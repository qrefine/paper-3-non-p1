# 4gif fresh start model preparation


1.	phenix.refine 4gif.mtz 4gif.pdb 

        a.	4gif_refine_001.pdb
  
        b.	4gif_refine_001.mtz -> renamed 4gif_refine_001_fresh.mtz
  
2.	qr.finalise 4gif_refine_001.pdb

        a.	4gif_refine_001_complete.pdb
  
3.	MODIFIED = atoms renumbered to avoid “No number atoms”

        a.	4gif_refine_001_complete.pdb_modified.pdb
  
4.	Water molecules which are in larger distance from the protein have been removed manually. These are atoms 767-855 from           4gif_refine_001_complete.pdb_modified.pdb. 

        a.	4gif_fresh_ready.pdb 
  
5. Refinements done using 4gif_fresh_ready.pdb  and 4gif_refine_001_fresh.mtz
