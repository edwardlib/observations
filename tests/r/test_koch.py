from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.koch import koch


def test_koch():
  """Test module koch.py by downloading
   koch.csv and testing shape of
   extracted data has 288 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = koch(test_path)
  try:
    assert x_train.shape == (288, 4)
  except:
    shutil.rmtree(test_path)
    raise()
