from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.sp_raw import sp_raw


def test_sp_raw():
  """Test module sp_raw.py by downloading
   sp_raw.csv and testing shape of
   extracted data has 8415 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = sp_raw(test_path)
  try:
    assert x_train.shape == (8415, 1)
  except:
    shutil.rmtree(test_path)
    raise()
