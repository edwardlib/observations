from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.leafshape import leafshape


def test_leafshape():
  """Test module leafshape.py by downloading
   leafshape.csv and testing shape of
   extracted data has 286 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = leafshape(test_path)
  try:
    assert x_train.shape == (286, 9)
  except:
    shutil.rmtree(test_path)
    raise()
