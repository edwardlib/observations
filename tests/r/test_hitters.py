from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.hitters import hitters


def test_hitters():
  """Test module hitters.py by downloading
   hitters.csv and testing shape of
   extracted data has 322 rows and 20 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = hitters(test_path)
  try:
    assert x_train.shape == (322, 20)
  except:
    shutil.rmtree(test_path)
    raise()
