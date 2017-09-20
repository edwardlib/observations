from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.dengue import dengue


def test_dengue():
  """Test module dengue.py by downloading
   dengue.csv and testing shape of
   extracted data has 2000 rows and 13 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = dengue(test_path)
  try:
    assert x_train.shape == (2000, 13)
  except:
    shutil.rmtree(test_path)
    raise()
