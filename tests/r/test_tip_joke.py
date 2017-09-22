from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.tip_joke import tip_joke


def test_tip_joke():
  """Test module tip_joke.py by downloading
   tip_joke.csv and testing shape of
   extracted data has 211 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = tip_joke(test_path)
  try:
    assert x_train.shape == (211, 5)
  except:
    shutil.rmtree(test_path)
    raise()
