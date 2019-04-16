# Steps

1) 
phenix.fetch_pdb 5c11 --mtz

2) 
Mutate 4WQ -> LYS (using Coot)

3)
qr.finalise 5c11_4WQ_to_LYS.pdb

4)
Make sure there is no H on S of CYS12.

5)
Run refinement