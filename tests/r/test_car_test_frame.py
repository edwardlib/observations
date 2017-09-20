from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.car_test_frame import car_test_frame


def test_car_test_frame():
  """Test module car_test_frame.py by downloading
   car_test_frame.csv and testing shape of
   extracted data has 60 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = car_test_frame(test_path)
  try:
    assert x_train.shape == (60, 8)
  except:
    shutil.rmtree(test_path)
    raise()
