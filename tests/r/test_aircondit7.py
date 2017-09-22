from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.aircondit7 import aircondit7


def test_aircondit7():
  """Test module aircondit7.py by downloading
   aircondit7.csv and testing shape of
   extracted data has 24 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = aircondit7(test_path)
  try:
    assert x_train.shape == (24, 1)
  except:
    shutil.rmtree(test_path)
    raise()
