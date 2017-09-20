from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.weldon_dice import weldon_dice


def test_weldon_dice():
  """Test module weldon_dice.py by downloading
   weldon_dice.csv and testing shape of
   extracted data has 11 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = weldon_dice(test_path)
  try:
    assert x_train.shape == (11, 2)
  except:
    shutil.rmtree(test_path)
    raise()
