from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.motors import motors


def test_motors():
  """Test module motors.py by downloading
   motors.csv and testing shape of
   extracted data has 40 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = motors(test_path)
  try:
    assert x_train.shape == (40, 3)
  except:
    shutil.rmtree(test_path)
    raise()
