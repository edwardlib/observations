from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.wagepan import wagepan


def test_wagepan():
  """Test module wagepan.py by downloading
   wagepan.csv and testing shape of
   extracted data has 4360 rows and 44 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = wagepan(test_path)
  try:
    assert x_train.shape == (4360, 44)
  except:
    shutil.rmtree(test_path)
    raise()
