from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.earnings import earnings


def test_earnings():
  """Test module earnings.py by downloading
   earnings.csv and testing shape of
   extracted data has 4266 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = earnings(test_path)
  try:
    assert x_train.shape == (4266, 2)
  except:
    shutil.rmtree(test_path)
    raise()
