from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.star import star


def test_star():
  """Test module star.py by downloading
   star.csv and testing shape of
   extracted data has 5748 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = star(test_path)
  try:
    assert x_train.shape == (5748, 8)
  except:
    shutil.rmtree(test_path)
    raise()
