from __future__ import division
from libtbx.test_utils import approx_equal
import iotbx.pdb
from scitbx.array_family import flex
from cctbx import crystal
import math
from libtbx import group_args
import mmtbx.model

def from_file(file_name):
  model = mmtbx.model.manager(
    model_input       = iotbx.pdb.input(file_name = file_name),
    build_grm         = True,
    stop_for_unknowns = False)
  return group_args(
    ph    = model.get_hierarchy(),
    xrs   = model.get_xray_structure(),
    cs    = model.crystal_symmetry(),
    model = model)

def run():
  ff = from_file(file_name="5bmi_refine_001_complete.pdb_modified.pdb")
  energy_1 = ff.model.restraints_manager_energies_sites().target
  fc_p1_1 = ff.xrs.deep_copy_scatterers().expand_to_p1(
    ).structure_factors(d_min=2, algorithm="direct").f_calc()
  #
  sites_frac = ff.xrs.sites_frac()
  xyz_best = None
  for x in [-2, -1, 0, 1, 2]:
    for y in [-2, -1, 0, 1, 2]:
      for z in [-2, -1, 0, 1, 2]:
        sf = sites_frac+[x,y,z]
        sc = ff.cs.unit_cell().orthogonalize(sf)
        cmf = ff.cs.unit_cell().fractionalize(sc.mean())
        if(cmf[0]>=0 and cmf[0]<=1 and
           cmf[1]>=0 and cmf[1]<=1 and
           cmf[2]>=0 and cmf[2]<=1):
          print cmf, [x,y,z]
          xyz_best = [x,y,z]
  #
  xrs = ff.xrs.replace_sites_frac(new_sites = sites_frac+xyz_best)
  ff.ph.atoms().set_xyz(xrs.sites_cart())
  #
  ff.ph.write_pdb_file(
    file_name="5bmi_refine_001_complete.pdb_modified.pdb_uc_shifted.pdb",
    crystal_symmetry=ff.cs)
  #
  ff = from_file(file_name="5bmi_refine_001_complete.pdb_modified.pdb_uc_shifted.pdb")
  energy_2 = ff.model.restraints_manager_energies_sites().target
  xrs_p1 = ff.xrs.expand_to_p1()
  fc_p1_2 = fc_p1_1.structure_factors_from_scatterers(
    xray_structure = xrs_p1.deep_copy_scatterers().expand_to_p1(),
    algorithm="direct").f_calc()
  #
  assert approx_equal(fc_p1_1.data(), fc_p1_2.data())
  print energy_1
  print energy_2

if __name__ == '__main__':
  run()
  print "OK"
