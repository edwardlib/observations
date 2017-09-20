from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.houseprices import houseprices


def test_houseprices():
  """Test module houseprices.py by downloading
   houseprices.csv and testing shape of
   extracted data has 15 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = houseprices(test_path)
  try:
    assert x_train.shape == (15, 3)
  except:
    shutil.rmtree(test_path)
    raise()
