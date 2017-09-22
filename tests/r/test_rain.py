from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.rain import rain


def test_rain():
  """Test module rain.py by downloading
   rain.csv and testing shape of
   extracted data has 17531 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = rain(test_path)
  try:
    assert x_train.shape == (17531, 1)
  except:
    shutil.rmtree(test_path)
    raise()
