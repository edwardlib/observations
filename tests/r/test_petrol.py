from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.petrol import petrol


def test_petrol():
  """Test module petrol.py by downloading
   petrol.csv and testing shape of
   extracted data has 32 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = petrol(test_path)
  try:
    assert x_train.shape == (32, 6)
  except:
    shutil.rmtree(test_path)
    raise()
