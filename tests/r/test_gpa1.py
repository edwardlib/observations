from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.gpa1 import gpa1


def test_gpa1():
  """Test module gpa1.py by downloading
   gpa1.csv and testing shape of
   extracted data has 141 rows and 29 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = gpa1(test_path)
  try:
    assert x_train.shape == (141, 29)
  except:
    shutil.rmtree(test_path)
    raise()
