from __future__ import division
import iotbx.pdb
import mmtbx.model
import math, sys, os
from libtbx import group_args
from scitbx.array_family import flex
from libtbx.utils import null_out
from libtbx.test_utils import approx_equal
from libtbx.utils import Sorry
import mmtbx.nci.hbond
    
def get_it(f, 
    d_HA_cutoff  = [1.4, 3.0],
    d_DA_cutoff  = [2.5, 3.5],
    a_DHA_cutoff = 120,
    a_YAH_cutoff = [90, 180]):
  pdb_inp = iotbx.pdb.input(file_name=f)
  model = mmtbx.model.manager(model_input = pdb_inp, build_grm = True,
    log = null_out())
  return mmtbx.nci.hbond.find(model = model,
    d_HA_cutoff  = d_HA_cutoff,
    d_DA_cutoff  = d_DA_cutoff,
    a_DHA_cutoff = a_DHA_cutoff,
    a_YAH_cutoff = a_YAH_cutoff)
    
def get_it2(f, pair_proxies = None):
  vals = flex.double()
  pdb_inp = iotbx.pdb.input(file_name=f)
  model = mmtbx.model.manager(model_input = pdb_inp, build_grm = True,
    log = null_out())
  o = mmtbx.nci.hbond.find(model=model, pair_proxies=pair_proxies)
  for p in o.result:
    if(str(p.symop)=="x,y,z"): continue # XXX Use only symmetry! XXX
    #vals.append(p.d_HA)
    vals.append(p.a_DHA)
  return vals, o.pair_proxies
  

def run():
  """
  This has to be run from paper-3-non-p1/4gif folder.
  """
  fn_tc    = "4gif_TeraChem_refine/pdb/4gif_refine_001_complete.pdb_modified_Pavel16March_refined.pdb"
  fn_xtb   = "4gif_xtb_refine/pdb_MaxItRef50/4gif_refine_001_complete.pdb_modified_Pavel16March_refined.pdb"
  fn_cctbx = "4gif_xtb_refine/4gif_refine_001_complete.pdb_modified_Pavel16March.pdb"
  
  vals_xtb  , pp_xtb   = get_it2(f=fn_xtb,   pair_proxies = None)
  vals_tc   , pp_tc    = get_it2(f=fn_tc,    pair_proxies = pp_xtb)
  vals_cctbx, pp_cctbx = get_it2(f=fn_cctbx, pair_proxies = pp_xtb)
  
  print "vals_tc   ", vals_tc.size()   
  print "vals_xtb  ", vals_xtb.size()
  print "vals_cctbx", vals_cctbx.size()
  
  for c, x, t in zip(vals_cctbx, vals_xtb, vals_tc):
    print "%8.4f %8.4f %8.4f" % (c, x, t)
    
if(__name__ == "__main__"):
  run()
