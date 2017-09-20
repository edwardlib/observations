from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.hbk import hbk


def test_hbk():
  """Test module hbk.py by downloading
   hbk.csv and testing shape of
   extracted data has 75 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = hbk(test_path)
  try:
    assert x_train.shape == (75, 4)
  except:
    shutil.rmtree(test_path)
    raise()
