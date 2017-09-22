from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.nswpsid1 import nswpsid1


def test_nswpsid1():
  """Test module nswpsid1.py by downloading
   nswpsid1.csv and testing shape of
   extracted data has 2787 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = nswpsid1(test_path)
  try:
    assert x_train.shape == (2787, 10)
  except:
    shutil.rmtree(test_path)
    raise()
