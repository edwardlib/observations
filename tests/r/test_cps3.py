from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cps3 import cps3


def test_cps3():
  """Test module cps3.py by downloading
   cps3.csv and testing shape of
   extracted data has 429 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cps3(test_path)
  try:
    assert x_train.shape == (429, 10)
  except:
    shutil.rmtree(test_path)
    raise()
