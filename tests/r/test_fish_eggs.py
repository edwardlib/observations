from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.fish_eggs import fish_eggs


def test_fish_eggs():
  """Test module fish_eggs.py by downloading
   fish_eggs.csv and testing shape of
   extracted data has 35 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = fish_eggs(test_path)
  try:
    assert x_train.shape == (35, 4)
  except:
    shutil.rmtree(test_path)
    raise()
