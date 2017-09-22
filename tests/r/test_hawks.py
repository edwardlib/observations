from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.hawks import hawks


def test_hawks():
  """Test module hawks.py by downloading
   hawks.csv and testing shape of
   extracted data has 908 rows and 19 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = hawks(test_path)
  try:
    assert x_train.shape == (908, 19)
  except:
    shutil.rmtree(test_path)
    raise()
