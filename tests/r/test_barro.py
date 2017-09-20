from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.barro import barro


def test_barro():
  """Test module barro.py by downloading
   barro.csv and testing shape of
   extracted data has 161 rows and 14 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = barro(test_path)
  try:
    assert x_train.shape == (161, 14)
  except:
    shutil.rmtree(test_path)
    raise()
