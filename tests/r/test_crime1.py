from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.crime1 import crime1


def test_crime1():
  """Test module crime1.py by downloading
   crime1.csv and testing shape of
   extracted data has 2725 rows and 16 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = crime1(test_path)
  try:
    assert x_train.shape == (2725, 16)
  except:
    shutil.rmtree(test_path)
    raise()
