from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.harman_political import harman_political


def test_harman_political():
  """Test module harman_political.py by downloading
   harman_political.csv and testing shape of
   extracted data has 8 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = harman_political(test_path)
  try:
    assert x_train.shape == (8, 8)
  except:
    shutil.rmtree(test_path)
    raise()
