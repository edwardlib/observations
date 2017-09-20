from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.math_enrollment import math_enrollment


def test_math_enrollment():
  """Test module math_enrollment.py by downloading
   math_enrollment.csv and testing shape of
   extracted data has 11 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = math_enrollment(test_path)
  try:
    assert x_train.shape == (11, 3)
  except:
    shutil.rmtree(test_path)
    raise()
