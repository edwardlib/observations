from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.meap00_01 import meap00_01


def test_meap00_01():
  """Test module meap00_01.py by downloading
   meap00_01.csv and testing shape of
   extracted data has 1692 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = meap00_01(test_path)
  try:
    assert x_train.shape == (1692, 9)
  except:
    shutil.rmtree(test_path)
    raise()
