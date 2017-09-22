from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.baseball_times import baseball_times


def test_baseball_times():
  """Test module baseball_times.py by downloading
   baseball_times.csv and testing shape of
   extracted data has 15 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = baseball_times(test_path)
  try:
    assert x_train.shape == (15, 7)
  except:
    shutil.rmtree(test_path)
    raise()
