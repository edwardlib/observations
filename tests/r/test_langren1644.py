from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.langren1644 import langren1644


def test_langren1644():
  """Test module langren1644.py by downloading
   langren1644.csv and testing shape of
   extracted data has 12 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = langren1644(test_path)
  try:
    assert x_train.shape == (12, 9)
  except:
    shutil.rmtree(test_path)
    raise()
