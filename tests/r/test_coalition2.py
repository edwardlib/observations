from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.coalition2 import coalition2


def test_coalition2():
  """Test module coalition2.py by downloading
   coalition2.csv and testing shape of
   extracted data has 314 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = coalition2(test_path)
  try:
    assert x_train.shape == (314, 8)
  except:
    shutil.rmtree(test_path)
    raise()
