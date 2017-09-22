from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.genfan import genfan


def test_genfan():
  """Test module genfan.py by downloading
   genfan.csv and testing shape of
   extracted data has 70 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = genfan(test_path)
  try:
    assert x_train.shape == (70, 2)
  except:
    shutil.rmtree(test_path)
    raise()
