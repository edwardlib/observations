from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.hprice2 import hprice2


def test_hprice2():
  """Test module hprice2.py by downloading
   hprice2.csv and testing shape of
   extracted data has 506 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = hprice2(test_path)
  try:
    assert x_train.shape == (506, 12)
  except:
    shutil.rmtree(test_path)
    raise()
