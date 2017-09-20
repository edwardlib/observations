from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.leafshape17 import leafshape17


def test_leafshape17():
  """Test module leafshape17.py by downloading
   leafshape17.csv and testing shape of
   extracted data has 61 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = leafshape17(test_path)
  try:
    assert x_train.shape == (61, 8)
  except:
    shutil.rmtree(test_path)
    raise()
