from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.pollster08 import pollster08


def test_pollster08():
  """Test module pollster08.py by downloading
   pollster08.csv and testing shape of
   extracted data has 102 rows and 11 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = pollster08(test_path)
  try:
    assert x_train.shape == (102, 11)
  except:
    shutil.rmtree(test_path)
    raise()
