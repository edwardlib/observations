from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.mlb_2007_standings import mlb_2007_standings


def test_mlb_2007_standings():
  """Test module mlb_2007_standings.py by downloading
   mlb_2007_standings.csv and testing shape of
   extracted data has 30 rows and 21 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = mlb_2007_standings(test_path)
  try:
    assert x_train.shape == (30, 21)
  except:
    shutil.rmtree(test_path)
    raise()
