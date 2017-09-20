from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.tomlinson_rush import tomlinson_rush


def test_tomlinson_rush():
  """Test module tomlinson_rush.py by downloading
   tomlinson_rush.csv and testing shape of
   extracted data has 16 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = tomlinson_rush(test_path)
  try:
    assert x_train.shape == (16, 4)
  except:
    shutil.rmtree(test_path)
    raise()
