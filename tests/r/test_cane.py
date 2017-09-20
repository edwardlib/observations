from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cane import cane


def test_cane():
  """Test module cane.py by downloading
   cane.csv and testing shape of
   extracted data has 180 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cane(test_path)
  try:
    assert x_train.shape == (180, 5)
  except:
    shutil.rmtree(test_path)
    raise()
