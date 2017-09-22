from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.wool1 import wool1


def test_wool1():
  """Test module wool1.py by downloading
   wool1.csv and testing shape of
   extracted data has 27 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = wool1(test_path)
  try:
    assert x_train.shape == (27, 4)
  except:
    shutil.rmtree(test_path)
    raise()
