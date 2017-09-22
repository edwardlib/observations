from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.litters import litters


def test_litters():
  """Test module litters.py by downloading
   litters.csv and testing shape of
   extracted data has 20 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = litters(test_path)
  try:
    assert x_train.shape == (20, 3)
  except:
    shutil.rmtree(test_path)
    raise()
