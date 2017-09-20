from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.seatshare import seatshare


def test_seatshare():
  """Test module seatshare.py by downloading
   seatshare.csv and testing shape of
   extracted data has 384 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = seatshare(test_path)
  try:
    assert x_train.shape == (384, 4)
  except:
    shutil.rmtree(test_path)
    raise()
