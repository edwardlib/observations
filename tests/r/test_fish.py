from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.fish import fish


def test_fish():
  """Test module fish.py by downloading
   fish.csv and testing shape of
   extracted data has 97 rows and 20 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = fish(test_path)
  try:
    assert x_train.shape == (97, 20)
  except:
    shutil.rmtree(test_path)
    raise()
