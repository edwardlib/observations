from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.markets import markets


def test_markets():
  """Test module markets.py by downloading
   markets.csv and testing shape of
   extracted data has 56 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = markets(test_path)
  try:
    assert x_train.shape == (56, 5)
  except:
    shutil.rmtree(test_path)
    raise()
