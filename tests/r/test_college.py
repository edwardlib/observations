from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.college import college


def test_college():
  """Test module college.py by downloading
   college.csv and testing shape of
   extracted data has 777 rows and 18 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = college(test_path)
  try:
    assert x_train.shape == (777, 18)
  except:
    shutil.rmtree(test_path)
    raise()
