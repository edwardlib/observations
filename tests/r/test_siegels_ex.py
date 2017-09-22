from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.siegels_ex import siegels_ex


def test_siegels_ex():
  """Test module siegels_ex.py by downloading
   siegels_ex.csv and testing shape of
   extracted data has 9 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = siegels_ex(test_path)
  try:
    assert x_train.shape == (9, 2)
  except:
    shutil.rmtree(test_path)
    raise()
