from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.walking_babies import walking_babies


def test_walking_babies():
  """Test module walking_babies.py by downloading
   walking_babies.csv and testing shape of
   extracted data has 24 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = walking_babies(test_path)
  try:
    assert x_train.shape == (24, 2)
  except:
    shutil.rmtree(test_path)
    raise()
