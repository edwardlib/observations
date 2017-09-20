from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cooling_water import cooling_water


def test_cooling_water():
  """Test module cooling_water.py by downloading
   cooling_water.csv and testing shape of
   extracted data has 222 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cooling_water(test_path)
  try:
    assert x_train.shape == (222, 2)
  except:
    shutil.rmtree(test_path)
    raise()
