from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.pottery1 import pottery1


def test_pottery1():
  """Test module pottery1.py by downloading
   pottery1.csv and testing shape of
   extracted data has 45 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = pottery1(test_path)
  try:
    assert x_train.shape == (45, 9)
  except:
    shutil.rmtree(test_path)
    raise()
