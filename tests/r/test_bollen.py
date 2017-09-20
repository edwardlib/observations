from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bollen import bollen


def test_bollen():
  """Test module bollen.py by downloading
   bollen.csv and testing shape of
   extracted data has 75 rows and 11 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bollen(test_path)
  try:
    assert x_train.shape == (75, 11)
  except:
    shutil.rmtree(test_path)
    raise()
