from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.races2000 import races2000


def test_races2000():
  """Test module races2000.py by downloading
   races2000.csv and testing shape of
   extracted data has 77 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = races2000(test_path)
  try:
    assert x_train.shape == (77, 5)
  except:
    shutil.rmtree(test_path)
    raise()
