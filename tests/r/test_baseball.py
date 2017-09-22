from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.baseball import baseball


def test_baseball():
  """Test module baseball.py by downloading
   baseball.csv and testing shape of
   extracted data has 21699 rows and 22 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = baseball(test_path)
  try:
    assert x_train.shape == (21699, 22)
  except:
    shutil.rmtree(test_path)
    raise()
