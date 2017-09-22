from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.sitka89 import sitka89


def test_sitka89():
  """Test module sitka89.py by downloading
   sitka89.csv and testing shape of
   extracted data has 632 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = sitka89(test_path)
  try:
    assert x_train.shape == (632, 4)
  except:
    shutil.rmtree(test_path)
    raise()
