from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.driving import driving


def test_driving():
  """Test module driving.py by downloading
   driving.csv and testing shape of
   extracted data has 1200 rows and 56 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = driving(test_path)
  try:
    assert x_train.shape == (1200, 56)
  except:
    shutil.rmtree(test_path)
    raise()
