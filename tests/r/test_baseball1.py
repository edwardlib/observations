from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.baseball1 import baseball1


def test_baseball1():
  """Test module baseball1.py by downloading
   baseball1.csv and testing shape of
   extracted data has 322 rows and 25 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = baseball1(test_path)
  try:
    assert x_train.shape == (322, 25)
  except:
    shutil.rmtree(test_path)
    raise()
