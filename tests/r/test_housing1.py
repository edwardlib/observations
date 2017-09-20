from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.housing1 import housing1


def test_housing1():
  """Test module housing1.py by downloading
   housing1.csv and testing shape of
   extracted data has 1448 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = housing1(test_path)
  try:
    assert x_train.shape == (1448, 4)
  except:
    shutil.rmtree(test_path)
    raise()
