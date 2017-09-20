from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.air_accs import air_accs


def test_air_accs():
  """Test module air_accs.py by downloading
   air_accs.csv and testing shape of
   extracted data has 5666 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = air_accs(test_path)
  try:
    assert x_train.shape == (5666, 7)
  except:
    shutil.rmtree(test_path)
    raise()
