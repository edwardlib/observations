from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.gravity import gravity


def test_gravity():
  """Test module gravity.py by downloading
   gravity.csv and testing shape of
   extracted data has 81 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = gravity(test_path)
  try:
    assert x_train.shape == (81, 2)
  except:
    shutil.rmtree(test_path)
    raise()
