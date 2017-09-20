from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.highway1 import highway1


def test_highway1():
  """Test module highway1.py by downloading
   highway1.csv and testing shape of
   extracted data has 39 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = highway1(test_path)
  try:
    assert x_train.shape == (39, 12)
  except:
    shutil.rmtree(test_path)
    raise()
