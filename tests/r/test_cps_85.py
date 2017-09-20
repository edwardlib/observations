from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cps_85 import cps_85


def test_cps_85():
  """Test module cps_85.py by downloading
   cps_85.csv and testing shape of
   extracted data has 534 rows and 11 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cps_85(test_path)
  try:
    assert x_train.shape == (534, 11)
  except:
    shutil.rmtree(test_path)
    raise()
