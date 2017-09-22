from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.free1 import free1


def test_free1():
  """Test module free1.py by downloading
   free1.csv and testing shape of
   extracted data has 450 rows and 11 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = free1(test_path)
  try:
    assert x_train.shape == (450, 11)
  except:
    shutil.rmtree(test_path)
    raise()
