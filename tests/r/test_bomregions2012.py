from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bomregions2012 import bomregions2012


def test_bomregions2012():
  """Test module bomregions2012.py by downloading
   bomregions2012.csv and testing shape of
   extracted data has 113 rows and 22 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bomregions2012(test_path)
  try:
    assert x_train.shape == (113, 22)
  except:
    shutil.rmtree(test_path)
    raise()
