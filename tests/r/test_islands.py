from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.islands import islands


def test_islands():
  """Test module islands.py by downloading
   islands.csv and testing shape of
   extracted data has 48 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = islands(test_path)
  try:
    assert x_train.shape == (48, 1)
  except:
    shutil.rmtree(test_path)
    raise()
