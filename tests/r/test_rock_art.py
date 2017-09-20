from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.rock_art import rock_art


def test_rock_art():
  """Test module rock_art.py by downloading
   rock_art.csv and testing shape of
   extracted data has 103 rows and 641 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = rock_art(test_path)
  try:
    assert x_train.shape == (103, 641)
  except:
    shutil.rmtree(test_path)
    raise()
