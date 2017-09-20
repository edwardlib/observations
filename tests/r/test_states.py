from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.states import states


def test_states():
  """Test module states.py by downloading
   states.csv and testing shape of
   extracted data has 51 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = states(test_path)
  try:
    assert x_train.shape == (51, 7)
  except:
    shutil.rmtree(test_path)
    raise()
