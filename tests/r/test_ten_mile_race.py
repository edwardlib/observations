from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ten_mile_race import ten_mile_race


def test_ten_mile_race():
  """Test module ten_mile_race.py by downloading
   ten_mile_race.csv and testing shape of
   extracted data has 8636 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ten_mile_race(test_path)
  try:
    assert x_train.shape == (8636, 5)
  except:
    shutil.rmtree(test_path)
    raise()
