from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.flower import flower


def test_flower():
  """Test module flower.py by downloading
   flower.csv and testing shape of
   extracted data has 18 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = flower(test_path)
  try:
    assert x_train.shape == (18, 8)
  except:
    shutil.rmtree(test_path)
    raise()
