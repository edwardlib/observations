from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.yogurt import yogurt


def test_yogurt():
  """Test module yogurt.py by downloading
   yogurt.csv and testing shape of
   extracted data has 2412 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = yogurt(test_path)
  try:
    assert x_train.shape == (2412, 10)
  except:
    shutil.rmtree(test_path)
    raise()
