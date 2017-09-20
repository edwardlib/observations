from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.crime2 import crime2


def test_crime2():
  """Test module crime2.py by downloading
   crime2.csv and testing shape of
   extracted data has 92 rows and 34 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = crime2(test_path)
  try:
    assert x_train.shape == (92, 34)
  except:
    shutil.rmtree(test_path)
    raise()
