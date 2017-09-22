from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.jevons import jevons


def test_jevons():
  """Test module jevons.py by downloading
   jevons.csv and testing shape of
   extracted data has 50 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = jevons(test_path)
  try:
    assert x_train.shape == (50, 4)
  except:
    shutil.rmtree(test_path)
    raise()
