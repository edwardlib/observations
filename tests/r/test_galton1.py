from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.galton1 import galton1


def test_galton1():
  """Test module galton1.py by downloading
   galton1.csv and testing shape of
   extracted data has 928 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = galton1(test_path)
  try:
    assert x_train.shape == (928, 2)
  except:
    shutil.rmtree(test_path)
    raise()
