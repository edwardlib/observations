from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.putts2 import putts2


def test_putts2():
  """Test module putts2.py by downloading
   putts2.csv and testing shape of
   extracted data has 5 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = putts2(test_path)
  try:
    assert x_train.shape == (5, 4)
  except:
    shutil.rmtree(test_path)
    raise()
