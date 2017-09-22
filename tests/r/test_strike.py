from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.strike import strike


def test_strike():
  """Test module strike.py by downloading
   strike.csv and testing shape of
   extracted data has 62 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = strike(test_path)
  try:
    assert x_train.shape == (62, 2)
  except:
    shutil.rmtree(test_path)
    raise()
