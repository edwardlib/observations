from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.immi2 import immi2


def test_immi2():
  """Test module immi2.py by downloading
   immi2.csv and testing shape of
   extracted data has 2485 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = immi2(test_path)
  try:
    assert x_train.shape == (2485, 5)
  except:
    shutil.rmtree(test_path)
    raise()
