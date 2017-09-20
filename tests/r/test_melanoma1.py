from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.melanoma1 import melanoma1


def test_melanoma1():
  """Test module melanoma1.py by downloading
   melanoma1.csv and testing shape of
   extracted data has 205 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = melanoma1(test_path)
  try:
    assert x_train.shape == (205, 7)
  except:
    shutil.rmtree(test_path)
    raise()
