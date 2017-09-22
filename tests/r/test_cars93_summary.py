from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cars93_summary import cars93_summary


def test_cars93_summary():
  """Test module cars93_summary.py by downloading
   cars93_summary.csv and testing shape of
   extracted data has 6 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cars93_summary(test_path)
  try:
    assert x_train.shape == (6, 4)
  except:
    shutil.rmtree(test_path)
    raise()
