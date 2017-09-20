from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.can_pop import can_pop


def test_can_pop():
  """Test module can_pop.py by downloading
   can_pop.csv and testing shape of
   extracted data has 16 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = can_pop(test_path)
  try:
    assert x_train.shape == (16, 2)
  except:
    shutil.rmtree(test_path)
    raise()
