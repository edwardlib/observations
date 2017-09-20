from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.attitude import attitude


def test_attitude():
  """Test module attitude.py by downloading
   attitude.csv and testing shape of
   extracted data has 30 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = attitude(test_path)
  try:
    assert x_train.shape == (30, 7)
  except:
    shutil.rmtree(test_path)
    raise()
