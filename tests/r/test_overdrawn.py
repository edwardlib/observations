from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.overdrawn import overdrawn


def test_overdrawn():
  """Test module overdrawn.py by downloading
   overdrawn.csv and testing shape of
   extracted data has 450 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = overdrawn(test_path)
  try:
    assert x_train.shape == (450, 4)
  except:
    shutil.rmtree(test_path)
    raise()
