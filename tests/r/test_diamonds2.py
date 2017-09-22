from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.diamonds2 import diamonds2


def test_diamonds2():
  """Test module diamonds2.py by downloading
   diamonds2.csv and testing shape of
   extracted data has 307 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = diamonds2(test_path)
  try:
    assert x_train.shape == (307, 6)
  except:
    shutil.rmtree(test_path)
    raise()
