from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.tuna1 import tuna1


def test_tuna1():
  """Test module tuna1.py by downloading
   tuna1.csv and testing shape of
   extracted data has 13705 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = tuna1(test_path)
  try:
    assert x_train.shape == (13705, 8)
  except:
    shutil.rmtree(test_path)
    raise()
