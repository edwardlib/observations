from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.traffic1 import traffic1


def test_traffic1():
  """Test module traffic1.py by downloading
   traffic1.csv and testing shape of
   extracted data has 51 rows and 13 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = traffic1(test_path)
  try:
    assert x_train.shape == (51, 13)
  except:
    shutil.rmtree(test_path)
    raise()
