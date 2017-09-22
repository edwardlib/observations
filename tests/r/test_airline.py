from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.airline import airline


def test_airline():
  """Test module airline.py by downloading
   airline.csv and testing shape of
   extracted data has 90 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = airline(test_path)
  try:
    assert x_train.shape == (90, 6)
  except:
    shutil.rmtree(test_path)
    raise()
