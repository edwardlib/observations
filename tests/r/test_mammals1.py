from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.mammals1 import mammals1


def test_mammals1():
  """Test module mammals1.py by downloading
   mammals1.csv and testing shape of
   extracted data has 107 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = mammals1(test_path)
  try:
    assert x_train.shape == (107, 4)
  except:
    shutil.rmtree(test_path)
    raise()
