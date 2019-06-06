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

def show_histogram(data, n_slots, data_min, data_max, log=sys.stdout):
  from cctbx.array_family import flex
  hm = flex.histogram(
    data=data, n_slots=n_slots, data_min=data_min, data_max=data_max)
  lc_1 = hm.data_min()
  s_1 = enumerate(hm.slots())
  for (i_1,n_1) in s_1:
    hc_1 = hm.data_min() + hm.slot_width() * (i_1+1)
    #print >> log, "%10.5f - %-10.5f : %d" % (lc_1, hc_1, n_1)
    print >> log, "%10.2f : %d" % ((lc_1+hc_1)/2, n_1)
    lc_1 = hc_1
    
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
    vals.append(p.d_HA)
  return vals, o.pair_proxies
  
def get_starting_model(folder):
  pdbs = []
  for sub in os.listdir(folder):
    if(sub.endswith(".pdb")):
      pdbs.append(sub)
  pdbs = list(set(pdbs))
  if(len(pdbs)==0): return None
  assert len(pdbs)==1, pdbs
  return pdbs[0]
  
def get_files():
  # Must run in paper-3-non-p1 folder!
  root = os.getcwd()
  folders = ["more","more_lowres"]
  #folders = ["more_lowres",]
  pairs = []
  for folder in folders:
    #
    folder = "/".join([root, folder])
    print folder, "-"*(79-len(folder))
    assert os.path.isdir(folder)
    for sub_1 in os.listdir(folder):
      sub_1 = "/".join([folder, sub_1])
      if(not os.path.isdir(sub_1)): continue
      print "  ", os.path.basename(sub_1)
      for sub_2 in os.listdir(sub_1):
        sub_2 = "/".join([sub_1, sub_2])
        if(not os.path.isdir(sub_2)): continue
        print "    ", os.path.basename(sub_2)
        # star model
        start = "/".join([sub_2, get_starting_model(sub_2)])
        #
        sub_3 = "/".join([sub_2, "pdb"])
        if(not os.path.isdir(sub_3)):
          print "       NO RESULT"
          continue
        refined = []
        for fn in os.listdir(sub_3):
          if(fn.endswith("_refined.pdb")):
            refined.append(fn)
        assert len(refined) <= 1
        if(len(refined)==0):
          print "       NO RESULT"
          continue
        refined = "/".join([sub_3, refined[0]])
        assert os.path.isfile(refined)
        #
        pair = [start, refined]
        pairs.append(pair)
  return pairs  

def run():
  #
  pairs = get_files()
  #
  f_vals = flex.double()
  s_vals = flex.double()
  for pair in pairs:
    #print pair[0]
    #print pair[1]
    start, final = pair
    f_vals_, pp  = get_it2(f=final)
    s_vals_, tmp = get_it2(f=start, pair_proxies=pp)
    print len(pp), f_vals_.size(), s_vals_.size(), flex.max_default(f_vals_,0), \
      flex.max_default(s_vals_,0)
    f_vals.extend(f_vals_)
    s_vals.extend(s_vals_)
    #
  print
  print "f_vals:", f_vals.size()
  print "s_vals:", s_vals.size()
  print
  #
  mi = min(flex.min(s_vals), flex.min(f_vals))
  mi = max(1.3, mi)
  ma = max(flex.max(s_vals), flex.max(f_vals))
  ma = min(ma, 4)
  #
  show_histogram(data = s_vals, n_slots=10, data_min=mi, data_max=ma)
  print
  show_histogram(data = f_vals, n_slots=10, data_min=mi, data_max=ma)
  print
  print "-"*79
  show_histogram(data = s_vals, n_slots=20, data_min=mi, data_max=ma)
  print
  show_histogram(data = f_vals, n_slots=20, data_min=mi, data_max=ma)

    
if(__name__ == "__main__"):
  run()
