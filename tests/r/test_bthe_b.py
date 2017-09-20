from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bthe_b import bthe_b


def test_bthe_b():
  """Test module bthe_b.py by downloading
   bthe_b.csv and testing shape of
   extracted data has 100 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bthe_b(test_path)
  try:
    assert x_train.shape == (100, 8)
  except:
    shutil.rmtree(test_path)
    raise()
