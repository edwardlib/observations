from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.lottario import lottario


def test_lottario():
  """Test module lottario.py by downloading
   lottario.csv and testing shape of
   extracted data has 39 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = lottario(test_path)
  try:
    assert x_train.shape == (39, 2)
  except:
    shutil.rmtree(test_path)
    raise()
