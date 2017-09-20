from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.clothing import clothing


def test_clothing():
  """Test module clothing.py by downloading
   clothing.csv and testing shape of
   extracted data has 60 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = clothing(test_path)
  try:
    assert x_train.shape == (60, 8)
  except:
    shutil.rmtree(test_path)
    raise()
