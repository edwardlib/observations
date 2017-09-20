from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.med_expenses import med_expenses


def test_med_expenses():
  """Test module med_expenses.py by downloading
   med_expenses.csv and testing shape of
   extracted data has 33 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = med_expenses(test_path)
  try:
    assert x_train.shape == (33, 2)
  except:
    shutil.rmtree(test_path)
    raise()
