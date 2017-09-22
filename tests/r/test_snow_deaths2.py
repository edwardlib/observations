from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.snow_deaths2 import snow_deaths2


def test_snow_deaths2():
  """Test module snow_deaths2.py by downloading
   snow_deaths2.csv and testing shape of
   extracted data has 578 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = snow_deaths2(test_path)
  try:
    assert x_train.shape == (578, 3)
  except:
    shutil.rmtree(test_path)
    raise()
