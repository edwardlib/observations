from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.hills import hills


def test_hills():
  """Test module hills.py by downloading
   hills.csv and testing shape of
   extracted data has 35 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = hills(test_path)
  try:
    assert x_train.shape == (35, 3)
  except:
    shutil.rmtree(test_path)
    raise()
