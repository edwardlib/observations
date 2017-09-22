from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.carprice import carprice


def test_carprice():
  """Test module carprice.py by downloading
   carprice.csv and testing shape of
   extracted data has 48 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = carprice(test_path)
  try:
    assert x_train.shape == (48, 9)
  except:
    shutil.rmtree(test_path)
    raise()
