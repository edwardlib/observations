from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.backpack import backpack


def test_backpack():
  """Test module backpack.py by downloading
   backpack.csv and testing shape of
   extracted data has 100 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = backpack(test_path)
  try:
    assert x_train.shape == (100, 9)
  except:
    shutil.rmtree(test_path)
    raise()
