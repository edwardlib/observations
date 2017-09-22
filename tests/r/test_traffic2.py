from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.traffic2 import traffic2


def test_traffic2():
  """Test module traffic2.py by downloading
   traffic2.csv and testing shape of
   extracted data has 108 rows and 48 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = traffic2(test_path)
  try:
    assert x_train.shape == (108, 48)
  except:
    shutil.rmtree(test_path)
    raise()
