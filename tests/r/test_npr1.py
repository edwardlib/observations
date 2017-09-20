from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.npr1 import npr1


def test_npr1():
  """Test module npr1.py by downloading
   npr1.csv and testing shape of
   extracted data has 104 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = npr1(test_path)
  try:
    assert x_train.shape == (104, 4)
  except:
    shutil.rmtree(test_path)
    raise()
