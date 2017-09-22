from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bomregions import bomregions


def test_bomregions():
  """Test module bomregions.py by downloading
   bomregions.csv and testing shape of
   extracted data has 109 rows and 22 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bomregions(test_path)
  try:
    assert x_train.shape == (109, 22)
  except:
    shutil.rmtree(test_path)
    raise()
