from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.barley import barley


def test_barley():
  """Test module barley.py by downloading
   barley.csv and testing shape of
   extracted data has 90 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = barley(test_path)
  try:
    assert x_train.shape == (90, 3)
  except:
    shutil.rmtree(test_path)
    raise()
