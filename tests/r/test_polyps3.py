from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.polyps3 import polyps3


def test_polyps3():
  """Test module polyps3.py by downloading
   polyps3.csv and testing shape of
   extracted data has 22 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = polyps3(test_path)
  try:
    assert x_train.shape == (22, 5)
  except:
    shutil.rmtree(test_path)
    raise()
