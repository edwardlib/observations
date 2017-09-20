from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.danish_welfare import danish_welfare


def test_danish_welfare():
  """Test module danish_welfare.py by downloading
   danish_welfare.csv and testing shape of
   extracted data has 180 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = danish_welfare(test_path)
  try:
    assert x_train.shape == (180, 5)
  except:
    shutil.rmtree(test_path)
    raise()
