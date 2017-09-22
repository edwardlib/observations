from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.births78 import births78


def test_births78():
  """Test module births78.py by downloading
   births78.csv and testing shape of
   extracted data has 365 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = births78(test_path)
  try:
    assert x_train.shape == (365, 4)
  except:
    shutil.rmtree(test_path)
    raise()
