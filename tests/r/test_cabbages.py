from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cabbages import cabbages


def test_cabbages():
  """Test module cabbages.py by downloading
   cabbages.csv and testing shape of
   extracted data has 60 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cabbages(test_path)
  try:
    assert x_train.shape == (60, 4)
  except:
    shutil.rmtree(test_path)
    raise()
