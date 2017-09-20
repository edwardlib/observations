from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bmw import bmw


def test_bmw():
  """Test module bmw.py by downloading
   bmw.csv and testing shape of
   extracted data has 6146 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bmw(test_path)
  try:
    assert x_train.shape == (6146, 1)
  except:
    shutil.rmtree(test_path)
    raise()
