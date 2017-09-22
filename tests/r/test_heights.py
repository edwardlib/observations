from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.heights import heights


def test_heights():
  """Test module heights.py by downloading
   heights.csv and testing shape of
   extracted data has 348 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = heights(test_path)
  try:
    assert x_train.shape == (348, 2)
  except:
    shutil.rmtree(test_path)
    raise()
