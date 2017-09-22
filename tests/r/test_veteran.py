from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.veteran import veteran


def test_veteran():
  """Test module veteran.py by downloading
   veteran.csv and testing shape of
   extracted data has 137 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = veteran(test_path)
  try:
    assert x_train.shape == (137, 8)
  except:
    shutil.rmtree(test_path)
    raise()
