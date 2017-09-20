from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.gehan import gehan


def test_gehan():
  """Test module gehan.py by downloading
   gehan.csv and testing shape of
   extracted data has 42 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = gehan(test_path)
  try:
    assert x_train.shape == (42, 4)
  except:
    shutil.rmtree(test_path)
    raise()
