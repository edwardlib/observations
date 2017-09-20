from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.minn38 import minn38


def test_minn38():
  """Test module minn38.py by downloading
   minn38.csv and testing shape of
   extracted data has 168 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = minn38(test_path)
  try:
    assert x_train.shape == (168, 5)
  except:
    shutil.rmtree(test_path)
    raise()
