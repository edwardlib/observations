from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.humanpower2 import humanpower2


def test_humanpower2():
  """Test module humanpower2.py by downloading
   humanpower2.csv and testing shape of
   extracted data has 26 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = humanpower2(test_path)
  try:
    assert x_train.shape == (26, 3)
  except:
    shutil.rmtree(test_path)
    raise()
