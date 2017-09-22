from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.road import road


def test_road():
  """Test module road.py by downloading
   road.csv and testing shape of
   extracted data has 26 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = road(test_path)
  try:
    assert x_train.shape == (26, 6)
  except:
    shutil.rmtree(test_path)
    raise()
