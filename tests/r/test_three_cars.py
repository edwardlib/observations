from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.three_cars import three_cars


def test_three_cars():
  """Test module three_cars.py by downloading
   three_cars.csv and testing shape of
   extracted data has 90 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = three_cars(test_path)
  try:
    assert x_train.shape == (90, 8)
  except:
    shutil.rmtree(test_path)
    raise()
