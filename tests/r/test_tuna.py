from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.tuna import tuna


def test_tuna():
  """Test module tuna.py by downloading
   tuna.csv and testing shape of
   extracted data has 64 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = tuna(test_path)
  try:
    assert x_train.shape == (64, 1)
  except:
    shutil.rmtree(test_path)
    raise()
