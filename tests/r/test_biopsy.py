from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.biopsy import biopsy


def test_biopsy():
  """Test module biopsy.py by downloading
   biopsy.csv and testing shape of
   extracted data has 699 rows and 11 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = biopsy(test_path)
  try:
    assert x_train.shape == (699, 11)
  except:
    shutil.rmtree(test_path)
    raise()
