from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.klein1 import klein1


def test_klein1():
  """Test module klein1.py by downloading
   klein1.csv and testing shape of
   extracted data has 22 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = klein1(test_path)
  try:
    assert x_train.shape == (22, 10)
  except:
    shutil.rmtree(test_path)
    raise()
