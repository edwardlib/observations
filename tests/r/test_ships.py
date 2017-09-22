from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ships import ships


def test_ships():
  """Test module ships.py by downloading
   ships.csv and testing shape of
   extracted data has 40 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ships(test_path)
  try:
    assert x_train.shape == (40, 7)
  except:
    shutil.rmtree(test_path)
    raise()
