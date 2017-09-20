from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.friend_foe import friend_foe


def test_friend_foe():
  """Test module friend_foe.py by downloading
   friend_foe.csv and testing shape of
   extracted data has 227 rows and 13 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = friend_foe(test_path)
  try:
    assert x_train.shape == (227, 13)
  except:
    shutil.rmtree(test_path)
    raise()
