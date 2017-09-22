from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.danish import danish


def test_danish():
  """Test module danish.py by downloading
   danish.csv and testing shape of
   extracted data has 2167 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = danish(test_path)
  try:
    assert x_train.shape == (2167, 1)
  except:
    shutil.rmtree(test_path)
    raise()
