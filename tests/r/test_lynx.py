from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.lynx import lynx


def test_lynx():
  """Test module lynx.py by downloading
   lynx.csv and testing shape of
   extracted data has 114 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = lynx(test_path)
  try:
    assert x_train.shape == (114, 2)
  except:
    shutil.rmtree(test_path)
    raise()
