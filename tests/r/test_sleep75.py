from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.sleep75 import sleep75


def test_sleep75():
  """Test module sleep75.py by downloading
   sleep75.csv and testing shape of
   extracted data has 706 rows and 34 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = sleep75(test_path)
  try:
    assert x_train.shape == (706, 34)
  except:
    shutil.rmtree(test_path)
    raise()
