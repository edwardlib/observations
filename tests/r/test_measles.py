from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.measles import measles


def test_measles():
  """Test module measles.py by downloading
   measles.csv and testing shape of
   extracted data has 311 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = measles(test_path)
  try:
    assert x_train.shape == (311, 2)
  except:
    shutil.rmtree(test_path)
    raise()
