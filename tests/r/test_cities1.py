from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cities1 import cities1


def test_cities1():
  """Test module cities1.py by downloading
   cities1.csv and testing shape of
   extracted data has 11 rows and 11 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cities1(test_path)
  try:
    assert x_train.shape == (11, 11)
  except:
    shutil.rmtree(test_path)
    raise()
