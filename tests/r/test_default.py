from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.default import default


def test_default():
  """Test module default.py by downloading
   default.csv and testing shape of
   extracted data has 10000 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = default(test_path)
  try:
    assert x_train.shape == (10000, 4)
  except:
    shutil.rmtree(test_path)
    raise()
