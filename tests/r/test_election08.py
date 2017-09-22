from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.election08 import election08


def test_election08():
  """Test module election08.py by downloading
   election08.csv and testing shape of
   extracted data has 51 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = election08(test_path)
  try:
    assert x_train.shape == (51, 7)
  except:
    shutil.rmtree(test_path)
    raise()
