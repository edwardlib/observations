from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.snow_streets import snow_streets


def test_snow_streets():
  """Test module snow_streets.py by downloading
   snow_streets.csv and testing shape of
   extracted data has 1241 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = snow_streets(test_path)
  try:
    assert x_train.shape == (1241, 4)
  except:
    shutil.rmtree(test_path)
    raise()
