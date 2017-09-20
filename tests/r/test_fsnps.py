from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.fsnps import fsnps


def test_fsnps():
  """Test module fsnps.py by downloading
   fsnps.csv and testing shape of
   extracted data has 432 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = fsnps(test_path)
  try:
    assert x_train.shape == (432, 10)
  except:
    shutil.rmtree(test_path)
    raise()
