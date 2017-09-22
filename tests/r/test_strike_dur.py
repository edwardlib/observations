from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.strike_dur import strike_dur


def test_strike_dur():
  """Test module strike_dur.py by downloading
   strike_dur.csv and testing shape of
   extracted data has 566 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = strike_dur(test_path)
  try:
    assert x_train.shape == (566, 2)
  except:
    shutil.rmtree(test_path)
    raise()
