from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.mid import mid


def test_mid():
  """Test module mid.py by downloading
   mid.csv and testing shape of
   extracted data has 3126 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = mid(test_path)
  try:
    assert x_train.shape == (3126, 7)
  except:
    shutil.rmtree(test_path)
    raise()
