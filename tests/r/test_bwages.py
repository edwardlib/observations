from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bwages import bwages


def test_bwages():
  """Test module bwages.py by downloading
   bwages.csv and testing shape of
   extracted data has 1472 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bwages(test_path)
  try:
    assert x_train.shape == (1472, 4)
  except:
    shutil.rmtree(test_path)
    raise()
