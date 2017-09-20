from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.women_queue import women_queue


def test_women_queue():
  """Test module women_queue.py by downloading
   women_queue.csv and testing shape of
   extracted data has 11 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = women_queue(test_path)
  try:
    assert x_train.shape == (11, 2)
  except:
    shutil.rmtree(test_path)
    raise()
