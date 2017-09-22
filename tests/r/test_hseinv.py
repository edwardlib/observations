from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.hseinv import hseinv


def test_hseinv():
  """Test module hseinv.py by downloading
   hseinv.csv and testing shape of
   extracted data has 42 rows and 14 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = hseinv(test_path)
  try:
    assert x_train.shape == (42, 14)
  except:
    shutil.rmtree(test_path)
    raise()
