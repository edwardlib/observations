from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.snow_deaths import snow_deaths


def test_snow_deaths():
  """Test module snow_deaths.py by downloading
   snow_deaths.csv and testing shape of
   extracted data has 578 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = snow_deaths(test_path)
  try:
    assert x_train.shape == (578, 3)
  except:
    shutil.rmtree(test_path)
    raise()
