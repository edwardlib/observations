from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cps1 import cps1


def test_cps1():
  """Test module cps1.py by downloading
   cps1.csv and testing shape of
   extracted data has 15992 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cps1(test_path)
  try:
    assert x_train.shape == (15992, 10)
  except:
    shutil.rmtree(test_path)
    raise()
