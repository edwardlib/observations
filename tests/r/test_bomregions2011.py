from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bomregions2011 import bomregions2011


def test_bomregions2011():
  """Test module bomregions2011.py by downloading
   bomregions2011.csv and testing shape of
   extracted data has 112 rows and 22 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bomregions2011(test_path)
  try:
    assert x_train.shape == (112, 22)
  except:
    shutil.rmtree(test_path)
    raise()
