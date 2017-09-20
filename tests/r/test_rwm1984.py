from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.rwm1984 import rwm1984


def test_rwm1984():
  """Test module rwm1984.py by downloading
   rwm1984.csv and testing shape of
   extracted data has 3874 rows and 15 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = rwm1984(test_path)
  try:
    assert x_train.shape == (3874, 15)
  except:
    shutil.rmtree(test_path)
    raise()
