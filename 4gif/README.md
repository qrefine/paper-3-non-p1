# 4gif is a simpler alternative for the non-P1 paper found by Pavel. 

It is 2.8 A resolution, P_3_2_1 symmetry.

Documented model preparation:

1.	phenix.fetch_pdb --mtz 4gif

2.	phenix.refine 4gif.{pdb,mtz} ordered_solvent=true ordered_solvent.low_res=3

3.	qr.finalise 4gif_refine_001.pdb

4.	phenix.pdbtools 4gif_refine_001_complete.pdb occupancies.set=0 modify.selection="element H"

Short results summary in 4gif_for_paper3_symmetry_OKdocumented

Original PDB is showing several clashscores which are removed fully by both xtb and Terachem qr.refine.

# Analysis

PDB
Deviations from Ideal Values.
  Bond      :  0.014   0.065    362
  Angle     :  1.645  12.032    485
  Chirality :  0.098   0.248     54
  Planarity :  0.005   0.031     59
  Dihedral  : 14.180  55.809    212
  Min Nonbonded Distance : 2.276

Molprobity Statistics.
  All-atom Clashscore : 6.92
  Ramachandran Plot:
    Outliers :  0.00 %
    Allowed  :  0.00 %
    Favored  : 100.00 %
  Rotamer Outliers :  5.26 %
  Cbeta Deviations :  0.00 %
  Peptide Plane:
    Cis-proline     : 0.00 %
    Cis-general     : 0.00 %
    Twisted Proline : 0.00 %
    Twisted General : 0.00 %
  r_work: 0.2335
  r_free: 0.2994
---------
phenix.refine
Deviations from Ideal Values.
  Bond      :  0.007   0.040    363
  Angle     :  0.828   4.242    487
  Chirality :  0.044   0.117     54
  Planarity :  0.003   0.008     60
  Dihedral  : 14.577  54.298    213
  Min Nonbonded Distance : 1.885

Molprobity Statistics.
  All-atom Clashscore : 11.05
  Ramachandran Plot:
    Outliers :  0.00 %
    Allowed  :  0.00 %
    Favored  : 100.00 %
  Rotamer Outliers :  0.00 %
  Cbeta Deviations :  0.00 %
  Peptide Plane:
    Cis-proline     : 0.00 %
    Cis-general     : 0.00 %
    Twisted Proline : 0.00 %
    Twisted General : 0.00 %
  r_work: 0.2443
  r_free: 0.2992
----
XTB
Deviations from Ideal Values.
  Bond      :  0.011   0.056    363
  Angle     :  1.481   8.318    487
  Chirality :  0.082   0.222     54
  Planarity :  0.016   0.093     60
  Dihedral  : 12.868  82.579    213
  Min Nonbonded Distance : 2.563

Molprobity Statistics.
  All-atom Clashscore : 1.38
  Ramachandran Plot:
    Outliers :  0.00 %
    Allowed  :  0.00 %
    Favored  : 100.00 %
  Rotamer Outliers :  2.63 %
  Cbeta Deviations :  0.00 %
  Peptide Plane:
    Cis-proline     : 0.00 %
    Cis-general     : 0.00 %
    Twisted Proline : 0.00 %
    Twisted General : 0.00 %
  r_work: 0.2571
  r_free: 0.2949
-----
TERACHEM
Deviations from Ideal Values.
  Bond      :  0.014   0.067    363
  Angle     :  1.345   6.101    487
  Chirality :  0.091   0.284     54
  Planarity :  0.018   0.120     60
  Dihedral  : 12.237  60.878    213
  Min Nonbonded Distance : 2.585

Molprobity Statistics.
  All-atom Clashscore : 1.38
  Ramachandran Plot:
    Outliers :  0.00 %
    Allowed  :  0.00 %
    Favored  : 100.00 %
  Rotamer Outliers :  0.00 %
  Cbeta Deviations :  0.00 %
  Peptide Plane:
    Cis-proline     : 0.00 %
    Cis-general     : 0.00 %
    Twisted Proline : 0.00 %
    Twisted General : 0.00 %
  r_work: 0.2473
  r_free: 0.2910
