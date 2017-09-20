from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bcdeter import bcdeter


def test_bcdeter():
  """Test module bcdeter.py by downloading
   bcdeter.csv and testing shape of
   extracted data has 95 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bcdeter(test_path)
  try:
    assert x_train.shape == (95, 3)
  except:
    shutil.rmtree(test_path)
    raise()
