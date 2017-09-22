from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.summer import summer


def test_summer():
  """Test module summer.py by downloading
   summer.csv and testing shape of
   extracted data has 578 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = summer(test_path)
  try:
    assert x_train.shape == (578, 5)
  except:
    shutil.rmtree(test_path)
    raise()
