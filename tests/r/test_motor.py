from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.motor import motor


def test_motor():
  """Test module motor.py by downloading
   motor.csv and testing shape of
   extracted data has 94 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = motor(test_path)
  try:
    assert x_train.shape == (94, 4)
  except:
    shutil.rmtree(test_path)
    raise()
