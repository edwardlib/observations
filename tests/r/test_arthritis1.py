from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.arthritis1 import arthritis1


def test_arthritis1():
  """Test module arthritis1.py by downloading
   arthritis1.csv and testing shape of
   extracted data has 906 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = arthritis1(test_path)
  try:
    assert x_train.shape == (906, 7)
  except:
    shutil.rmtree(test_path)
    raise()
