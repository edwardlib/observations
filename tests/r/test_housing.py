from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.housing import housing


def test_housing():
  """Test module housing.py by downloading
   housing.csv and testing shape of
   extracted data has 546 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = housing(test_path)
  try:
    assert x_train.shape == (546, 12)
  except:
    shutil.rmtree(test_path)
    raise()
