from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.fgb_y_distance import fgb_y_distance


def test_fgb_y_distance():
  """Test module fgb_y_distance.py by downloading
   fgb_y_distance.csv and testing shape of
   extracted data has 51 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = fgb_y_distance(test_path)
  try:
    assert x_train.shape == (51, 7)
  except:
    shutil.rmtree(test_path)
    raise()
