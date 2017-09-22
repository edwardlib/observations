from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.retirement import retirement


def test_retirement():
  """Test module retirement.py by downloading
   retirement.csv and testing shape of
   extracted data has 16 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = retirement(test_path)
  try:
    assert x_train.shape == (16, 2)
  except:
    shutil.rmtree(test_path)
    raise()
