from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.hprice1 import hprice1


def test_hprice1():
  """Test module hprice1.py by downloading
   hprice1.csv and testing shape of
   extracted data has 88 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = hprice1(test_path)
  try:
    assert x_train.shape == (88, 10)
  except:
    shutil.rmtree(test_path)
    raise()
