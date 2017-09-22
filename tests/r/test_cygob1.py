from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cygob1 import cygob1


def test_cygob1():
  """Test module cygob1.py by downloading
   cygob1.csv and testing shape of
   extracted data has 47 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cygob1(test_path)
  try:
    assert x_train.shape == (47, 2)
  except:
    shutil.rmtree(test_path)
    raise()
