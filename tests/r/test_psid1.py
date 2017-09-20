from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.psid1 import psid1


def test_psid1():
  """Test module psid1.py by downloading
   psid1.csv and testing shape of
   extracted data has 2490 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = psid1(test_path)
  try:
    assert x_train.shape == (2490, 10)
  except:
    shutil.rmtree(test_path)
    raise()
