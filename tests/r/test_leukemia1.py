from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.leukemia1 import leukemia1


def test_leukemia1():
  """Test module leukemia1.py by downloading
   leukemia1.csv and testing shape of
   extracted data has 51 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = leukemia1(test_path)
  try:
    assert x_train.shape == (51, 9)
  except:
    shutil.rmtree(test_path)
    raise()
