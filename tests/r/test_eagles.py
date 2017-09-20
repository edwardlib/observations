from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.eagles import eagles


def test_eagles():
  """Test module eagles.py by downloading
   eagles.csv and testing shape of
   extracted data has 8 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = eagles(test_path)
  try:
    assert x_train.shape == (8, 5)
  except:
    shutil.rmtree(test_path)
    raise()
