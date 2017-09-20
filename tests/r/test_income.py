from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.income import income


def test_income():
  """Test module income.py by downloading
   income.csv and testing shape of
   extracted data has 44 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = income(test_path)
  try:
    assert x_train.shape == (44, 4)
  except:
    shutil.rmtree(test_path)
    raise()
