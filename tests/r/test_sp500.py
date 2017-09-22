from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.sp500 import sp500


def test_sp500():
  """Test module sp500.py by downloading
   sp500.csv and testing shape of
   extracted data has 2783 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = sp500(test_path)
  try:
    assert x_train.shape == (2783, 1)
  except:
    shutil.rmtree(test_path)
    raise()
