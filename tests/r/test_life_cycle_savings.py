from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.life_cycle_savings import life_cycle_savings


def test_life_cycle_savings():
  """Test module life_cycle_savings.py by downloading
   life_cycle_savings.csv and testing shape of
   extracted data has 50 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = life_cycle_savings(test_path)
  try:
    assert x_train.shape == (50, 5)
  except:
    shutil.rmtree(test_path)
    raise()
