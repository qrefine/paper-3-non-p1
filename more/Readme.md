# Additional PDB entries 
chosen to have only standard residues, no alternate locations and represent variety of space groups: 5zkt, 6agy, 6jqs, 6n1l, 6ney, 6nfs, 6njg.


Documented model preparation:

1.      phenix.fetch_pdb --mtz 

2.      leave only one set of data  

3.      qr.finalise > xxxx_complete.pdb

4.     phenix.refine xxxx_complete.pdb xxxx.mtz

5.     qr.refine xxxx_complete_refine_001.pdb  mode=gtest two_buffers=1 g_scan="1 5 10 15 25 50" > sanity check + chose optimal cpu-time maxnum_residues_in_cluster=N   

6.     qr.refine xxxx_complete_refine_001.pdb xxxx_complete_refine_001.mtz mode=refine maxnum_residues_in_cluster=N quantum.nproc=2 parallel.nproc=10 max_bond_rmsd=0.02  stpmax=0.2 gradient_only=true clustering=true use_convergence_test=true  opt_log=1 restraints=qm  engine_name=xtb  > 5zkt_xtb_refine_MaxResN.log   

## 3a5x (7194 atoms)
method         | bond   | angle |clashscore |rama_outlier| rama_favor|rotamer | CC_mask
:--:           | :--:   | :--:  |   :--:    |   :--:     |   :--:    |:--:    |:--:
initial        | 0.013  | 1.530 | 117.79    |   2.85     |   86.59   | 8.72   | 0.292
cctbx_refine   | 0.001  | 0.4   |  2.36     |   0.61     |   93.50   |  2.05  | 0.3025
xtb_refine     | 0.010  | 1.70  |  2.5      |   0.81     |   93.90   |  4.36  | 0.3050
terachem_refine| 0.014  | 1.4   |  1.53     |   0        |   96.75   |  4.62  | 0.3051

##5zkt – 1.74 A MaxNumRes=15	

	|	PDB	|	CCTBX	|	GFN-xTB2	
:--:   	|	:--:   	|	:--:   	|	:--:   
Rwork	|	0.209	|	0.1951	|	0.1938
Rfree	|	0.22	|	0.2061	|	0.2121
Rgap	|	0.0110	|	0.0110	|	0.0183
RMS(bonds)	|	0.0067	|	0.0119	|	0.0168
RMS(angles)	|	0.98	|	1.01	|	2.18
Ramachandran favored (%)	|	99.05	|	99.05	|	99.05
Ramachandran outliers(%)	|	0	|	0	|	0
Rotamer outliers(%)	|	0	|	0	|	2.25
Clashcore/1000 atoms	|	2.82	|	2.82	|	3.38
Cβ deviations	|	0	|	0	|	2
MolProbity score	|	1.07	|	1.07	|	1.4
	|	##6agy – 1.8 A  MaxNumRes=25	|		|	
	|	PDB	|	CCTBX	|	GFN-xTB2
:--:   	|	:--:   	|	:--:   	|	:--:   
Rwork	|	0.137	|	0.1376	|	0.137
Rfree	|	0.17	|	0.1779	|	0.1815
Rgap	|	0.0330	|	0.0403	|	0.0445
RMS(bonds)	|	0.0058	|	0.0179	|	0.0151
RMS(angles)	|	1.16	|	1.6	|	2.18
Ramachandran favored (%)	|	97.96	|	97.96	|	97.96
Ramachandran outliers(%)	|	0.68	|	0.68	|	0.68
Rotamer outliers(%)	|	0	|	0	|	0.8
Clashcore/1000 atoms	|	1.29	|	5.6	|	0.86
Cβ deviations	|	0	|	0	|	0
MolProbity score	|	0.86	|	1.31	|	0.77

