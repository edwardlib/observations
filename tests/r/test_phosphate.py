from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.phosphate import phosphate


def test_phosphate():
  """Test module phosphate.py by downloading
   phosphate.csv and testing shape of
   extracted data has 33 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = phosphate(test_path)
  try:
    assert x_train.shape == (33, 9)
  except:
    shutil.rmtree(test_path)
    raise()
