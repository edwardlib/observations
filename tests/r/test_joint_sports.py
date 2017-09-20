from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.joint_sports import joint_sports


def test_joint_sports():
  """Test module joint_sports.py by downloading
   joint_sports.csv and testing shape of
   extracted data has 40 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = joint_sports(test_path)
  try:
    assert x_train.shape == (40, 5)
  except:
    shutil.rmtree(test_path)
    raise()
