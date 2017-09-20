from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.mroz1 import mroz1


def test_mroz1():
  """Test module mroz1.py by downloading
   mroz1.csv and testing shape of
   extracted data has 753 rows and 18 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = mroz1(test_path)
  try:
    assert x_train.shape == (753, 18)
  except:
    shutil.rmtree(test_path)
    raise()
