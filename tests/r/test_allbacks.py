from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.allbacks import allbacks


def test_allbacks():
  """Test module allbacks.py by downloading
   allbacks.csv and testing shape of
   extracted data has 15 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = allbacks(test_path)
  try:
    assert x_train.shape == (15, 4)
  except:
    shutil.rmtree(test_path)
    raise()
