from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.math_placement import math_placement


def test_math_placement():
  """Test module math_placement.py by downloading
   math_placement.csv and testing shape of
   extracted data has 2696 rows and 16 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = math_placement(test_path)
  try:
    assert x_train.shape == (2696, 16)
  except:
    shutil.rmtree(test_path)
    raise()
