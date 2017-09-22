from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.strike_nb import strike_nb


def test_strike_nb():
  """Test module strike_nb.py by downloading
   strike_nb.csv and testing shape of
   extracted data has 108 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = strike_nb(test_path)
  try:
    assert x_train.shape == (108, 3)
  except:
    shutil.rmtree(test_path)
    raise()
