from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cps91 import cps91


def test_cps91():
  """Test module cps91.py by downloading
   cps91.csv and testing shape of
   extracted data has 5634 rows and 24 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cps91(test_path)
  try:
    assert x_train.shape == (5634, 24)
  except:
    shutil.rmtree(test_path)
    raise()
