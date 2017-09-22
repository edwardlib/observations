from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.grunfeld2 import grunfeld2


def test_grunfeld2():
  """Test module grunfeld2.py by downloading
   grunfeld2.csv and testing shape of
   extracted data has 20 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = grunfeld2(test_path)
  try:
    assert x_train.shape == (20, 7)
  except:
    shutil.rmtree(test_path)
    raise()
