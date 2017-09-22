from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.orings1 import orings1


def test_orings1():
  """Test module orings1.py by downloading
   orings1.csv and testing shape of
   extracted data has 24 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = orings1(test_path)
  try:
    assert x_train.shape == (24, 2)
  except:
    shutil.rmtree(test_path)
    raise()
