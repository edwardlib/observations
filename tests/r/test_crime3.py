from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.crime3 import crime3


def test_crime3():
  """Test module crime3.py by downloading
   crime3.csv and testing shape of
   extracted data has 106 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = crime3(test_path)
  try:
    assert x_train.shape == (106, 12)
  except:
    shutil.rmtree(test_path)
    raise()
