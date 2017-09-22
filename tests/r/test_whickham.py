from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.whickham import whickham


def test_whickham():
  """Test module whickham.py by downloading
   whickham.csv and testing shape of
   extracted data has 1314 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = whickham(test_path)
  try:
    assert x_train.shape == (1314, 3)
  except:
    shutil.rmtree(test_path)
    raise()
