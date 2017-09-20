from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.alcohol1 import alcohol1


def test_alcohol1():
  """Test module alcohol1.py by downloading
   alcohol1.csv and testing shape of
   extracted data has 411 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = alcohol1(test_path)
  try:
    assert x_train.shape == (411, 4)
  except:
    shutil.rmtree(test_path)
    raise()
