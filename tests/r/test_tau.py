from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.tau import tau


def test_tau():
  """Test module tau.py by downloading
   tau.csv and testing shape of
   extracted data has 60 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = tau(test_path)
  try:
    assert x_train.shape == (60, 2)
  except:
    shutil.rmtree(test_path)
    raise()
