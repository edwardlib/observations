from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.fishing1 import fishing1


def test_fishing1():
  """Test module fishing1.py by downloading
   fishing1.csv and testing shape of
   extracted data has 1182 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = fishing1(test_path)
  try:
    assert x_train.shape == (1182, 12)
  except:
    shutil.rmtree(test_path)
    raise()
