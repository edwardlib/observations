from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.crabs import crabs


def test_crabs():
  """Test module crabs.py by downloading
   crabs.csv and testing shape of
   extracted data has 200 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = crabs(test_path)
  try:
    assert x_train.shape == (200, 8)
  except:
    shutil.rmtree(test_path)
    raise()
