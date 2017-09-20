from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.riders import riders


def test_riders():
  """Test module riders.py by downloading
   riders.csv and testing shape of
   extracted data has 90 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = riders(test_path)
  try:
    assert x_train.shape == (90, 12)
  except:
    shutil.rmtree(test_path)
    raise()
