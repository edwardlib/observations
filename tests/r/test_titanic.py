from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.titanic import titanic


def test_titanic():
  """Test module titanic.py by downloading
   titanic.csv and testing shape of
   extracted data has 1313 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = titanic(test_path)
  try:
    assert x_train.shape == (1313, 6)
  except:
    shutil.rmtree(test_path)
    raise()
