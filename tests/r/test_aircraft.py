from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.aircraft import aircraft


def test_aircraft():
  """Test module aircraft.py by downloading
   aircraft.csv and testing shape of
   extracted data has 23 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = aircraft(test_path)
  try:
    assert x_train.shape == (23, 5)
  except:
    shutil.rmtree(test_path)
    raise()
