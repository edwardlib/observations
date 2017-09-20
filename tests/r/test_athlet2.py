from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.athlet2 import athlet2


def test_athlet2():
  """Test module athlet2.py by downloading
   athlet2.csv and testing shape of
   extracted data has 30 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = athlet2(test_path)
  try:
    assert x_train.shape == (30, 10)
  except:
    shutil.rmtree(test_path)
    raise()
