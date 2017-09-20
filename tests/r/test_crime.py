from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.crime import crime


def test_crime():
  """Test module crime.py by downloading
   crime.csv and testing shape of
   extracted data has 630 rows and 24 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = crime(test_path)
  try:
    assert x_train.shape == (630, 24)
  except:
    shutil.rmtree(test_path)
    raise()
