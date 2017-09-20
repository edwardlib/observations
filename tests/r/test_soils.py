from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.soils import soils


def test_soils():
  """Test module soils.py by downloading
   soils.csv and testing shape of
   extracted data has 48 rows and 14 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = soils(test_path)
  try:
    assert x_train.shape == (48, 14)
  except:
    shutil.rmtree(test_path)
    raise()
