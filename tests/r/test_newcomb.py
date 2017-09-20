from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.newcomb import newcomb


def test_newcomb():
  """Test module newcomb.py by downloading
   newcomb.csv and testing shape of
   extracted data has 66 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = newcomb(test_path)
  try:
    assert x_train.shape == (66, 1)
  except:
    shutil.rmtree(test_path)
    raise()
