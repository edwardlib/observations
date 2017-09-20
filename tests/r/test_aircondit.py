from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.aircondit import aircondit


def test_aircondit():
  """Test module aircondit.py by downloading
   aircondit.csv and testing shape of
   extracted data has 12 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = aircondit(test_path)
  try:
    assert x_train.shape == (12, 1)
  except:
    shutil.rmtree(test_path)
    raise()
