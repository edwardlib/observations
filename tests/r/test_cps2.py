from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cps2 import cps2


def test_cps2():
  """Test module cps2.py by downloading
   cps2.csv and testing shape of
   extracted data has 2369 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cps2(test_path)
  try:
    assert x_train.shape == (2369, 10)
  except:
    shutil.rmtree(test_path)
    raise()
