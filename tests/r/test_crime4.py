from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.crime4 import crime4


def test_crime4():
  """Test module crime4.py by downloading
   crime4.csv and testing shape of
   extracted data has 630 rows and 59 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = crime4(test_path)
  try:
    assert x_train.shape == (630, 59)
  except:
    shutil.rmtree(test_path)
    raise()
