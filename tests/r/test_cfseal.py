from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cfseal import cfseal


def test_cfseal():
  """Test module cfseal.py by downloading
   cfseal.csv and testing shape of
   extracted data has 30 rows and 11 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cfseal(test_path)
  try:
    assert x_train.shape == (30, 11)
  except:
    shutil.rmtree(test_path)
    raise()
