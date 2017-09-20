from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cricketer import cricketer


def test_cricketer():
  """Test module cricketer.py by downloading
   cricketer.csv and testing shape of
   extracted data has 5960 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cricketer(test_path)
  try:
    assert x_train.shape == (5960, 8)
  except:
    shutil.rmtree(test_path)
    raise()
