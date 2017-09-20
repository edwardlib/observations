from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cars93 import cars93


def test_cars93():
  """Test module cars93.py by downloading
   cars93.csv and testing shape of
   extracted data has 93 rows and 27 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cars93(test_path)
  try:
    assert x_train.shape == (93, 27)
  except:
    shutil.rmtree(test_path)
    raise()
