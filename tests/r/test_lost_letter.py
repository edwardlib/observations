from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.lost_letter import lost_letter


def test_lost_letter():
  """Test module lost_letter.py by downloading
   lost_letter.csv and testing shape of
   extracted data has 140 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = lost_letter(test_path)
  try:
    assert x_train.shape == (140, 8)
  except:
    shutil.rmtree(test_path)
    raise()
