from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.snow_pumps import snow_pumps


def test_snow_pumps():
  """Test module snow_pumps.py by downloading
   snow_pumps.csv and testing shape of
   extracted data has 13 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = snow_pumps(test_path)
  try:
    assert x_train.shape == (13, 4)
  except:
    shutil.rmtree(test_path)
    raise()
