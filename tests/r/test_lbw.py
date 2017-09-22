from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.lbw import lbw


def test_lbw():
  """Test module lbw.py by downloading
   lbw.csv and testing shape of
   extracted data has 189 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = lbw(test_path)
  try:
    assert x_train.shape == (189, 10)
  except:
    shutil.rmtree(test_path)
    raise()
