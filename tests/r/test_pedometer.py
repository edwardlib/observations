from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.pedometer import pedometer


def test_pedometer():
  """Test module pedometer.py by downloading
   pedometer.csv and testing shape of
   extracted data has 68 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = pedometer(test_path)
  try:
    assert x_train.shape == (68, 8)
  except:
    shutil.rmtree(test_path)
    raise()
