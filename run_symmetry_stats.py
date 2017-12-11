from __future__ import division
import iotbx.pdb
import collections
import math
import os
from libtbx import group_args
from libtbx import easy_pickle
from libtbx import easy_mp

pdb_dir = "/home/pdb/pdb/"
structure_factors_dir = "/home/pdb/structure_factors/"


def run(file_name, pdb_code):
  pdb_inp = iotbx.pdb.input(file_name=file_name)
  cs = pdb_inp.crystal_symmetry()
  result = group_args(
    space_group_symbol = cs.space_group().type().lookup_symbol())
  easy_pickle.dump(pdb_code+".pkl", result)

if __name__ == '__main__':
  nproc=6
  # PDB model files
  #path = "/net/cci/pdb_mirror/pdb/"
  path=pdb_dir
  of = open("".join([path,"INDEX"]),"r")
  files = ["".join([path,f]).strip() for f in of.readlines()]
  of.close()
  # PDB reflection data files (list of corresponding codes)
  #dpath = "/net/cci/pdb_mirror/structure_factors/"
  dpath=structure_factors_dir
  of = open("".join([dpath,"INDEX"]),"r")
  dfiles = [
    os.path.basename("".join([path,f]).strip())[1:5] for f in of.readlines()]
  of.close()
  # XXX For debugging
  #run(file_name="1f8t.pdb", pdb_code="1f8t")
  args = []
  for f in files:
    pdb_code = os.path.basename(f)[3:7]
    if(pdb_code in dfiles):
      args.append([f, pdb_code])
  #  if(len(args)==500): break # For testing
  #
  for arg, res, err_str in easy_mp.multi_core_run(run, args, nproc):
    if err_str:
      print 'Error output from %s' % arg
      print err_str
      print '_'*80
