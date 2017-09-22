from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.lh import lh


def test_lh():
  """Test module lh.py by downloading
   lh.csv and testing shape of
   extracted data has 48 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = lh(test_path)
  try:
    assert x_train.shape == (48, 2)
  except:
    shutil.rmtree(test_path)
    raise()
