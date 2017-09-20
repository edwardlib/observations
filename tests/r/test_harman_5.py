from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.harman_5 import harman_5


def test_harman_5():
  """Test module harman_5.py by downloading
   harman_5.csv and testing shape of
   extracted data has 12 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = harman_5(test_path)
  try:
    assert x_train.shape == (12, 5)
  except:
    shutil.rmtree(test_path)
    raise()
