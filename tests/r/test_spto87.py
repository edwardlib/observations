from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.spto87 import spto87


def test_spto87():
  """Test module spto87.py by downloading
   spto87.csv and testing shape of
   extracted data has 6985 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = spto87(test_path)
  try:
    assert x_train.shape == (6985, 1)
  except:
    shutil.rmtree(test_path)
    raise()
