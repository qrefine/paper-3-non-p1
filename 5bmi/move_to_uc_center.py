from __future__ import division
from libtbx.test_utils import approx_equal
import iotbx.pdb
from scitbx.array_family import flex
from cctbx import crystal
import math

def run():
  pdb_inp = iotbx.pdb.input(
    file_name = "5bmi_refine_001_complete.pdb_modified.pdb")
  cs = pdb_inp.crystal_symmetry()
  ph = pdb_inp.construct_hierarchy()
  xrs = ph.extract_xray_structure(crystal_symmetry=cs) 
#  fc_p1_1 = xrs.deep_copy_scatterers().expand_to_p1(
#    ).structure_factors(d_min=2, algorithm="fft").f_calc()
  
  sites_frac = xrs.sites_frac()
  xyz_best = None
  for x in [-2, -1, 0, 1, 2]:
    for y in [-2, -1, 0, 1, 2]:
      for z in [-2, -1, 0, 1, 2]:
        sf = sites_frac+[x,y,z]
        sc = cs.unit_cell().orthogonalize(sf)
        cmf = cs.unit_cell().fractionalize(sc.mean())
        if(cmf[0]>=0 and cmf[0]<=1 and 
           cmf[1]>=0 and cmf[1]<=1 and
           cmf[2]>=0 and cmf[2]<=1):
          print cmf, [x,y,z]
          xyz_best = [x,y,z]
  #      
  xrs = xrs.replace_sites_frac(new_sites = sites_frac+xyz_best)
  ph.atoms().set_xyz(xrs.sites_cart())
  #
  ph.write_pdb_file(
    file_name="5bmi_refine_001_complete.pdb_modified.pdb_uc_shifted.pdb", 
    crystal_symmetry=cs)
  #of = open("shifted.pdb","w")
  #print >> of, xrs.as_pdb_file()
  #of.close()
  #
  xrs_p1 = xrs.expand_to_p1()
  of = open("p1x.pdb","w")
  print >> of, xrs_p1.as_pdb_file()
  of.close()
  
#  STOP()
#  ########
#  asu_mappings = xrs.asu_mappings(buffer_thickness = 10)
#  asu_mappings.process_sites_frac(xrs_p1.sites_frac(), min_distance_sym_equiv =
#    xrs.min_distance_sym_equiv())
#  pair_generator = crystal.neighbors_fast_pair_generator(asu_mappings =
#    asu_mappings, distance_cutoff = 10)
#  d = flex.double()
#  for pair in pair_generator:
#    #print math.sqrt(pair.dist_sq)
#    d.append(math.sqrt(pair.dist_sq))
#  print flex.min(d), flex.max(d)
#    
#  ########
#  #
#  fc_p1_2 = fc_p1_1.structure_factors_from_scatterers(
#    xray_structure = xrs_p1.deep_copy_scatterers().expand_to_p1(), 
#    algorithm="fft").f_calc()
#  #
#  assert fc_p1_1.indices().all_eq(fc_p1_2.indices())
#  assert approx_equal(fc_p1_1.data(), fc_p1_2.data(), 0.1) # direct fixes it
#  STOP()
#  #
#  #
#  #
#  #
#  #
#  #
#  #
#  #
#  #
#  #
#  #
#  #STOP()
#  
#  xrs_p1 = xrs.expand_to_p1()
#  ##
#  of = open("p1.pdb","w")
#  print >> of, xrs_p1.as_pdb_file()
#  of.close()
#  ##
#  
#  #STOP()
#  
#  xyz_p1_x = xrs_p1.sites_cart()
#  ph_p1 = ph.expand_to_p1(crystal_symmetry=cs)
#  ##
#  cs_p1 = crystal.symmetry(cs.unit_cell(), "P1")
#  ph_p1.write_pdb_file(file_name="p1h.pdb", crystal_symmetry=cs_p1)
#  ##
##  xyz_p1_h = ph_p1.atoms().extract_xyz()
##  print xyz_p1_h.mean()
##  print xyz_p1_x.mean()
##  
##  nx = xyz_p1_x.norms()
##  nh = xyz_p1_h.norms()
##  
##  s = flex.sort_permutation(nx)
##  
##  nx = nx.select(s)
##  nh = nh.select(s)
##  assert approx_equal(nh, nh)
##  
##  STOP()
##  assert approx_equal(xyz_p1_x, xyz_p1_h)


if __name__ == '__main__':
  run()
