from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.tobin import tobin


def test_tobin():
  """Test module tobin.py by downloading
   tobin.csv and testing shape of
   extracted data has 20 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = tobin(test_path)
  try:
    assert x_train.shape == (20, 3)
  except:
    shutil.rmtree(test_path)
    raise()
