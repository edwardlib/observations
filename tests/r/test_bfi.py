from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bfi import bfi


def test_bfi():
  """Test module bfi.py by downloading
   bfi.csv and testing shape of
   extracted data has 2800 rows and 28 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bfi(test_path)
  try:
    assert x_train.shape == (2800, 28)
  except:
    shutil.rmtree(test_path)
    raise()
