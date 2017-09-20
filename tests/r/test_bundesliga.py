from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bundesliga import bundesliga


def test_bundesliga():
  """Test module bundesliga.py by downloading
   bundesliga.csv and testing shape of
   extracted data has 14018 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bundesliga(test_path)
  try:
    assert x_train.shape == (14018, 7)
  except:
    shutil.rmtree(test_path)
    raise()
