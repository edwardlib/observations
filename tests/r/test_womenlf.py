from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.womenlf import womenlf


def test_womenlf():
  """Test module womenlf.py by downloading
   womenlf.csv and testing shape of
   extracted data has 263 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = womenlf(test_path)
  try:
    assert x_train.shape == (263, 4)
  except:
    shutil.rmtree(test_path)
    raise()
