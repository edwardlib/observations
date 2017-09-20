from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.sat_state import sat_state


def test_sat_state():
  """Test module sat_state.py by downloading
   sat_state.csv and testing shape of
   extracted data has 50 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = sat_state(test_path)
  try:
    assert x_train.shape == (50, 8)
  except:
    shutil.rmtree(test_path)
    raise()
