from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.mroz2 import mroz2


def test_mroz2():
  """Test module mroz2.py by downloading
   mroz2.csv and testing shape of
   extracted data has 753 rows and 22 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = mroz2(test_path)
  try:
    assert x_train.shape == (753, 22)
  except:
    shutil.rmtree(test_path)
    raise()
