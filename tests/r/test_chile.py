from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.chile import chile


def test_chile():
  """Test module chile.py by downloading
   chile.csv and testing shape of
   extracted data has 2700 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = chile(test_path)
  try:
    assert x_train.shape == (2700, 8)
  except:
    shutil.rmtree(test_path)
    raise()
