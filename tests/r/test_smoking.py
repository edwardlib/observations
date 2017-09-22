from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.smoking import smoking


def test_smoking():
  """Test module smoking.py by downloading
   smoking.csv and testing shape of
   extracted data has 26 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = smoking(test_path)
  try:
    assert x_train.shape == (26, 4)
  except:
    shutil.rmtree(test_path)
    raise()
