from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bmt import bmt


def test_bmt():
  """Test module bmt.py by downloading
   bmt.csv and testing shape of
   extracted data has 137 rows and 22 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bmt(test_path)
  try:
    assert x_train.shape == (137, 22)
  except:
    shutil.rmtree(test_path)
    raise()
