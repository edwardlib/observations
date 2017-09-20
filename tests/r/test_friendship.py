from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.friendship import friendship


def test_friendship():
  """Test module friendship.py by downloading
   friendship.csv and testing shape of
   extracted data has 0 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = friendship(test_path)
  try:
    assert x_train.shape == (0, 7)
  except:
    shutil.rmtree(test_path)
    raise()
