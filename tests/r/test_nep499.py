from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.nep499 import nep499


def test_nep499():
  """Test module nep499.py by downloading
   nep499.csv and testing shape of
   extracted data has 499 rows and 23 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = nep499(test_path)
  try:
    assert x_train.shape == (499, 23)
  except:
    shutil.rmtree(test_path)
    raise()
