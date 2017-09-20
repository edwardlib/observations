from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.speed import speed


def test_speed():
  """Test module speed.py by downloading
   speed.csv and testing shape of
   extracted data has 21 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = speed(test_path)
  try:
    assert x_train.shape == (21, 3)
  except:
    shutil.rmtree(test_path)
    raise()
