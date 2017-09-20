from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.blood1 import blood1


def test_blood1():
  """Test module blood1.py by downloading
   blood1.csv and testing shape of
   extracted data has 500 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = blood1(test_path)
  try:
    assert x_train.shape == (500, 3)
  except:
    shutil.rmtree(test_path)
    raise()
