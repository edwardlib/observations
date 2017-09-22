from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.sp500_w90 import sp500_w90


def test_sp500_w90():
  """Test module sp500_w90.py by downloading
   sp500_w90.csv and testing shape of
   extracted data has 100 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = sp500_w90(test_path)
  try:
    assert x_train.shape == (100, 2)
  except:
    shutil.rmtree(test_path)
    raise()
