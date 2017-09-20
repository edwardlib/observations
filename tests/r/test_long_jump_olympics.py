from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.long_jump_olympics import long_jump_olympics


def test_long_jump_olympics():
  """Test module long_jump_olympics.py by downloading
   long_jump_olympics.csv and testing shape of
   extracted data has 26 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = long_jump_olympics(test_path)
  try:
    assert x_train.shape == (26, 2)
  except:
    shutil.rmtree(test_path)
    raise()
