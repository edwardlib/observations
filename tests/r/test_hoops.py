from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.hoops import hoops


def test_hoops():
  """Test module hoops.py by downloading
   hoops.csv and testing shape of
   extracted data has 147 rows and 22 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = hoops(test_path)
  try:
    assert x_train.shape == (147, 22)
  except:
    shutil.rmtree(test_path)
    raise()
