from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.sp500_close import sp500_close


def test_sp500_close():
  """Test module sp500_close.py by downloading
   sp500_close.csv and testing shape of
   extracted data has 2780 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = sp500_close(test_path)
  try:
    assert x_train.shape == (2780, 1)
  except:
    shutil.rmtree(test_path)
    raise()
