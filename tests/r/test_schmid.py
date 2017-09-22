from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.schmid import schmid


def test_schmid():
  """Test module schmid.py by downloading
   schmid.csv and testing shape of
   extracted data has 12 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = schmid(test_path)
  try:
    assert x_train.shape == (12, 12)
  except:
    shutil.rmtree(test_path)
    raise()
