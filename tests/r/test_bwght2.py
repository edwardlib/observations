from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bwght2 import bwght2


def test_bwght2():
  """Test module bwght2.py by downloading
   bwght2.csv and testing shape of
   extracted data has 1832 rows and 23 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bwght2(test_path)
  try:
    assert x_train.shape == (1832, 23)
  except:
    shutil.rmtree(test_path)
    raise()
