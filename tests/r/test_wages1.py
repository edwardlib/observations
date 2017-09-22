from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.wages1 import wages1


def test_wages1():
  """Test module wages1.py by downloading
   wages1.csv and testing shape of
   extracted data has 3294 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = wages1(test_path)
  try:
    assert x_train.shape == (3294, 4)
  except:
    shutil.rmtree(test_path)
    raise()
