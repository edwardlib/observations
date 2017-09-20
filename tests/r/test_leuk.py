from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.leuk import leuk


def test_leuk():
  """Test module leuk.py by downloading
   leuk.csv and testing shape of
   extracted data has 33 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = leuk(test_path)
  try:
    assert x_train.shape == (33, 3)
  except:
    shutil.rmtree(test_path)
    raise()
