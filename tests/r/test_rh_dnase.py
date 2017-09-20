from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.rh_dnase import rh_dnase


def test_rh_dnase():
  """Test module rh_dnase.py by downloading
   rh_dnase.csv and testing shape of
   extracted data has 767 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = rh_dnase(test_path)
  try:
    assert x_train.shape == (767, 8)
  except:
    shutil.rmtree(test_path)
    raise()
