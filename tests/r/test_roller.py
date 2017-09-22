from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.roller import roller


def test_roller():
  """Test module roller.py by downloading
   roller.csv and testing shape of
   extracted data has 10 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = roller(test_path)
  try:
    assert x_train.shape == (10, 2)
  except:
    shutil.rmtree(test_path)
    raise()
