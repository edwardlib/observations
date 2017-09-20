from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.snow_dates import snow_dates


def test_snow_dates():
  """Test module snow_dates.py by downloading
   snow_dates.csv and testing shape of
   extracted data has 44 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = snow_dates(test_path)
  try:
    assert x_train.shape == (44, 3)
  except:
    shutil.rmtree(test_path)
    raise()
