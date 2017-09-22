from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.immi1 import immi1


def test_immi1():
  """Test module immi1.py by downloading
   immi1.csv and testing shape of
   extracted data has 2485 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = immi1(test_path)
  try:
    assert x_train.shape == (2485, 5)
  except:
    shutil.rmtree(test_path)
    raise()
