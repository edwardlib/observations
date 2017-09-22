from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.barium import barium


def test_barium():
  """Test module barium.py by downloading
   barium.csv and testing shape of
   extracted data has 131 rows and 31 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = barium(test_path)
  try:
    assert x_train.shape == (131, 31)
  except:
    shutil.rmtree(test_path)
    raise()
