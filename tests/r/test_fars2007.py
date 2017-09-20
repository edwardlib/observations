from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.fars2007 import fars2007


def test_fars2007():
  """Test module fars2007.py by downloading
   fars2007.csv and testing shape of
   extracted data has 72548 rows and 24 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = fars2007(test_path)
  try:
    assert x_train.shape == (72548, 24)
  except:
    shutil.rmtree(test_path)
    raise()
