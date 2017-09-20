from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.pntsprd import pntsprd


def test_pntsprd():
  """Test module pntsprd.py by downloading
   pntsprd.csv and testing shape of
   extracted data has 553 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = pntsprd(test_path)
  try:
    assert x_train.shape == (553, 12)
  except:
    shutil.rmtree(test_path)
    raise()
