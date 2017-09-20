from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.car90 import car90


def test_car90():
  """Test module car90.py by downloading
   car90.csv and testing shape of
   extracted data has 111 rows and 34 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = car90(test_path)
  try:
    assert x_train.shape == (111, 34)
  except:
    shutil.rmtree(test_path)
    raise()
