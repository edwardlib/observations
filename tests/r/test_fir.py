from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.fir import fir


def test_fir():
  """Test module fir.py by downloading
   fir.csv and testing shape of
   extracted data has 50 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = fir(test_path)
  try:
    assert x_train.shape == (50, 3)
  except:
    shutil.rmtree(test_path)
    raise()
