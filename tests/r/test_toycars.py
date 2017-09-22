from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.toycars import toycars


def test_toycars():
  """Test module toycars.py by downloading
   toycars.csv and testing shape of
   extracted data has 27 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = toycars(test_path)
  try:
    assert x_train.shape == (27, 3)
  except:
    shutil.rmtree(test_path)
    raise()
