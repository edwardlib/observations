from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cps78_85 import cps78_85


def test_cps78_85():
  """Test module cps78_85.py by downloading
   cps78_85.csv and testing shape of
   extracted data has 1084 rows and 15 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cps78_85(test_path)
  try:
    assert x_train.shape == (1084, 15)
  except:
    shutil.rmtree(test_path)
    raise()
