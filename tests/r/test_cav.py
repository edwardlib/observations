from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cav import cav


def test_cav():
  """Test module cav.py by downloading
   cav.csv and testing shape of
   extracted data has 138 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cav(test_path)
  try:
    assert x_train.shape == (138, 2)
  except:
    shutil.rmtree(test_path)
    raise()
