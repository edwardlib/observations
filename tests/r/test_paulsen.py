from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.paulsen import paulsen


def test_paulsen():
  """Test module paulsen.py by downloading
   paulsen.csv and testing shape of
   extracted data has 346 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = paulsen(test_path)
  try:
    assert x_train.shape == (346, 1)
  except:
    shutil.rmtree(test_path)
    raise()
