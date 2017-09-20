from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.trucks import trucks


def test_trucks():
  """Test module trucks.py by downloading
   trucks.csv and testing shape of
   extracted data has 24 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = trucks(test_path)
  try:
    assert x_train.shape == (24, 5)
  except:
    shutil.rmtree(test_path)
    raise()
