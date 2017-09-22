from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.labor_supply import labor_supply


def test_labor_supply():
  """Test module labor_supply.py by downloading
   labor_supply.csv and testing shape of
   extracted data has 5320 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = labor_supply(test_path)
  try:
    assert x_train.shape == (5320, 7)
  except:
    shutil.rmtree(test_path)
    raise()
