from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.fantasy_baseball import fantasy_baseball


def test_fantasy_baseball():
  """Test module fantasy_baseball.py by downloading
   fantasy_baseball.csv and testing shape of
   extracted data has 24 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = fantasy_baseball(test_path)
  try:
    assert x_train.shape == (24, 9)
  except:
    shutil.rmtree(test_path)
    raise()
