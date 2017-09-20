from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.neo import neo


def test_neo():
  """Test module neo.py by downloading
   neo.csv and testing shape of
   extracted data has 30 rows and 30 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = neo(test_path)
  try:
    assert x_train.shape == (30, 30)
  except:
    shutil.rmtree(test_path)
    raise()
