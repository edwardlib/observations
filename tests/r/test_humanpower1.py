from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.humanpower1 import humanpower1


def test_humanpower1():
  """Test module humanpower1.py by downloading
   humanpower1.csv and testing shape of
   extracted data has 28 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = humanpower1(test_path)
  try:
    assert x_train.shape == (28, 3)
  except:
    shutil.rmtree(test_path)
    raise()
