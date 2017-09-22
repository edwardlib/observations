from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.loti import loti


def test_loti():
  """Test module loti.py by downloading
   loti.csv and testing shape of
   extracted data has 131 rows and 19 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = loti(test_path)
  try:
    assert x_train.shape == (131, 19)
  except:
    shutil.rmtree(test_path)
    raise()
