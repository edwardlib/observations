from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.dietox import dietox


def test_dietox():
  """Test module dietox.py by downloading
   dietox.csv and testing shape of
   extracted data has 861 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = dietox(test_path)
  try:
    assert x_train.shape == (861, 7)
  except:
    shutil.rmtree(test_path)
    raise()
