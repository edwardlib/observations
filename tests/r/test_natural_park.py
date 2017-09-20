from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.natural_park import natural_park


def test_natural_park():
  """Test module natural_park.py by downloading
   natural_park.csv and testing shape of
   extracted data has 312 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = natural_park(test_path)
  try:
    assert x_train.shape == (312, 7)
  except:
    shutil.rmtree(test_path)
    raise()
