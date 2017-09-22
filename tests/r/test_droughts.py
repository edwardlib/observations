from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.droughts import droughts


def test_droughts():
  """Test module droughts.py by downloading
   droughts.csv and testing shape of
   extracted data has 2042 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = droughts(test_path)
  try:
    assert x_train.shape == (2042, 2)
  except:
    shutil.rmtree(test_path)
    raise()
