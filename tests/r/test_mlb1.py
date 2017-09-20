from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.mlb1 import mlb1


def test_mlb1():
  """Test module mlb1.py by downloading
   mlb1.csv and testing shape of
   extracted data has 353 rows and 47 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = mlb1(test_path)
  try:
    assert x_train.shape == (353, 47)
  except:
    shutil.rmtree(test_path)
    raise()
