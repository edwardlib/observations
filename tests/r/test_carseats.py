from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.carseats import carseats


def test_carseats():
  """Test module carseats.py by downloading
   carseats.csv and testing shape of
   extracted data has 400 rows and 11 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = carseats(test_path)
  try:
    assert x_train.shape == (400, 11)
  except:
    shutil.rmtree(test_path)
    raise()
