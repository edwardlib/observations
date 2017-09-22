from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.sunspots import sunspots


def test_sunspots():
  """Test module sunspots.py by downloading
   sunspots.csv and testing shape of
   extracted data has 2820 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = sunspots(test_path)
  try:
    assert x_train.shape == (2820, 2)
  except:
    shutil.rmtree(test_path)
    raise()
