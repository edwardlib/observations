from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.salinity import salinity


def test_salinity():
  """Test module salinity.py by downloading
   salinity.csv and testing shape of
   extracted data has 28 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = salinity(test_path)
  try:
    assert x_train.shape == (28, 4)
  except:
    shutil.rmtree(test_path)
    raise()
