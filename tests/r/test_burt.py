from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.burt import burt


def test_burt():
  """Test module burt.py by downloading
   burt.csv and testing shape of
   extracted data has 27 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = burt(test_path)
  try:
    assert x_train.shape == (27, 3)
  except:
    shutil.rmtree(test_path)
    raise()
