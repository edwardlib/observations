from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.metro_health83 import metro_health83


def test_metro_health83():
  """Test module metro_health83.py by downloading
   metro_health83.csv and testing shape of
   extracted data has 83 rows and 16 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = metro_health83(test_path)
  try:
    assert x_train.shape == (83, 16)
  except:
    shutil.rmtree(test_path)
    raise()
