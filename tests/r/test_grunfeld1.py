from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.grunfeld1 import grunfeld1


def test_grunfeld1():
  """Test module grunfeld1.py by downloading
   grunfeld1.csv and testing shape of
   extracted data has 200 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = grunfeld1(test_path)
  try:
    assert x_train.shape == (200, 5)
  except:
    shutil.rmtree(test_path)
    raise()
