from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.rail_trail import rail_trail


def test_rail_trail():
  """Test module rail_trail.py by downloading
   rail_trail.csv and testing shape of
   extracted data has 90 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = rail_trail(test_path)
  try:
    assert x_train.shape == (90, 10)
  except:
    shutil.rmtree(test_path)
    raise()
