from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bfox import bfox


def test_bfox():
  """Test module bfox.py by downloading
   bfox.csv and testing shape of
   extracted data has 30 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bfox(test_path)
  try:
    assert x_train.shape == (30, 6)
  except:
    shutil.rmtree(test_path)
    raise()
