from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.beauty import beauty


def test_beauty():
  """Test module beauty.py by downloading
   beauty.csv and testing shape of
   extracted data has 1260 rows and 17 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = beauty(test_path)
  try:
    assert x_train.shape == (1260, 17)
  except:
    shutil.rmtree(test_path)
    raise()
