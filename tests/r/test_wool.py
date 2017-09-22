from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.wool import wool


def test_wool():
  """Test module wool.py by downloading
   wool.csv and testing shape of
   extracted data has 309 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = wool(test_path)
  try:
    assert x_train.shape == (309, 2)
  except:
    shutil.rmtree(test_path)
    raise()
