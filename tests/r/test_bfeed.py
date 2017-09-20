from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bfeed import bfeed


def test_bfeed():
  """Test module bfeed.py by downloading
   bfeed.csv and testing shape of
   extracted data has 927 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bfeed(test_path)
  try:
    assert x_train.shape == (927, 10)
  except:
    shutil.rmtree(test_path)
    raise()
