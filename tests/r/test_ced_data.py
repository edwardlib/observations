from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ced_data import ced_data


def test_ced_data():
  """Test module ced_data.py by downloading
   ced_data.csv and testing shape of
   extracted data has 2000 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ced_data(test_path)
  try:
    assert x_train.shape == (2000, 7)
  except:
    shutil.rmtree(test_path)
    raise()
