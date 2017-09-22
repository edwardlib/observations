from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.air_passengers import air_passengers


def test_air_passengers():
  """Test module air_passengers.py by downloading
   air_passengers.csv and testing shape of
   extracted data has 144 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = air_passengers(test_path)
  try:
    assert x_train.shape == (144, 2)
  except:
    shutil.rmtree(test_path)
    raise()
