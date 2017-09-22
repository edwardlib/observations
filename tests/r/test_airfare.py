from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.airfare import airfare


def test_airfare():
  """Test module airfare.py by downloading
   airfare.csv and testing shape of
   extracted data has 4596 rows and 14 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = airfare(test_path)
  try:
    assert x_train.shape == (4596, 14)
  except:
    shutil.rmtree(test_path)
    raise()
