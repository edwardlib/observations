from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ducks import ducks


def test_ducks():
  """Test module ducks.py by downloading
   ducks.csv and testing shape of
   extracted data has 11 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ducks(test_path)
  try:
    assert x_train.shape == (11, 2)
  except:
    shutil.rmtree(test_path)
    raise()
