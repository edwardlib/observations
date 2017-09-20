from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.hprice3 import hprice3


def test_hprice3():
  """Test module hprice3.py by downloading
   hprice3.csv and testing shape of
   extracted data has 321 rows and 19 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = hprice3(test_path)
  try:
    assert x_train.shape == (321, 19)
  except:
    shutil.rmtree(test_path)
    raise()
