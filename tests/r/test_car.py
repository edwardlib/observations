from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.car import car


def test_car():
  """Test module car.py by downloading
   car.csv and testing shape of
   extracted data has 4654 rows and 70 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = car(test_path)
  try:
    assert x_train.shape == (4654, 70)
  except:
    shutil.rmtree(test_path)
    raise()
