from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.psid3 import psid3


def test_psid3():
  """Test module psid3.py by downloading
   psid3.csv and testing shape of
   extracted data has 128 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = psid3(test_path)
  try:
    assert x_train.shape == (128, 10)
  except:
    shutil.rmtree(test_path)
    raise()
