from __future__ import division
import iotbx.pdb
import mmtbx.model
import math
from libtbx import group_args
import os, sys
from libtbx.utils import null_out
from scitbx.array_family import flex
import mmtbx.utils
from iotbx import reflection_file_utils
import mmtbx.f_model
from libtbx import easy_run

def get_starting_model(folder):
  pdbs = []
  for sub in os.listdir(folder):
    if(sub.endswith(".pdb")):
      pdbs.append(sub)
  pdbs = list(set(pdbs))
  if(len(pdbs)==0): return None
  assert len(pdbs)==1, pdbs
  return pdbs[0]

def get_mtz(folder):
  mtzs = []
  for sub in os.listdir(folder):
    if(sub.endswith(".mtz")):
      mtzs.append(sub)
  mtzs = list(set(mtzs))
  if(len(mtzs)==0): return None
  return mtzs[0] # arbitrarily get the first one

def get_r(mtz_file, model):
  inputs = mmtbx.utils.process_command_line_args(args = [mtz_file])
  reflection_files = inputs.reflection_files
  rfs = reflection_file_utils.reflection_file_server(
    crystal_symmetry = inputs.crystal_symmetry,
    force_symmetry   = True,
    reflection_files = reflection_files,
    err              = null_out())
  determined_data_and_flags = mmtbx.utils.determine_data_and_flags(
    reflection_file_server = rfs,
    keep_going             = True,
    log                    = null_out())
  f_obs = determined_data_and_flags.f_obs
  r_free_flags = determined_data_and_flags.r_free_flags
  fmodel = mmtbx.f_model.manager(
    f_obs          = f_obs,
    r_free_flags   = r_free_flags,
    xray_structure = model.get_xray_structure())
  fmodel.update_all_scales()
  return fmodel.r_work(), fmodel.r_free()
  
def get_z(fn):
  cmd = " ".join([
    "phenix.development.rama_z_score",
    fn])
  r = easy_run.fully_buffered(cmd).raise_if_errors()
  return round(float(r.stdout_lines[-1].split()[1]), 3)

def run():
  # Must run in paper-3-non-p1 folder!
  root = os.getcwd()
  folders = ["more","more_lowres"]
  for folder in folders:
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
        print "    ", os.path.basename(sub_2),
        # get mtz
        mtz_file = get_mtz(sub_2)
        mtz_file = "/".join([sub_2, mtz_file])
        assert os.path.isfile(mtz_file)
        # star model
        start = "/".join([sub_2, get_starting_model(sub_2)])
        zs_start = get_z(start)
        assert os.path.isfile(start)
        pdb_inp = iotbx.pdb.input(file_name=start)
        model_1 = mmtbx.model.manager(model_input = pdb_inp, build_grm = True,
          log = null_out())
        print "       start:", \
          model_1.geometry_statistics(use_hydrogens=False).show_short(),
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
        zs_refined = get_z(refined)
        #
        pdb_inp = iotbx.pdb.input(file_name=refined)
        model_2 = mmtbx.model.manager(model_input = pdb_inp, build_grm = True,
          log = null_out())
        print "       final:", \
          model_2.geometry_statistics(use_hydrogens=False).show_short(),
        #
        s1 = model_1.get_sites_cart()
        s2 = model_2.get_sites_cart()
        dist = flex.sqrt((s1 - s2).dot())
        print "       min/max/mean(start, final): %5.3f %5.3f %5.3f"%\
          dist.min_max_mean().as_tuple(),
        #
        rs1 = get_r(mtz_file=mtz_file, model=model_1)
        rs2 = get_r(mtz_file=mtz_file, model=model_2)
        print "       r_work, r_free (start): %6.4f %6.4f"%rs1,
        print "       r_work, r_free (final): %6.4f %6.4f"%rs2, "z-score(start, final)", zs_start, zs_refined
        sys.stdout.flush()

if(__name__ == "__main__"):
  run()
