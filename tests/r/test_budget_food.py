from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.budget_food import budget_food


def test_budget_food():
  """Test module budget_food.py by downloading
   budget_food.csv and testing shape of
   extracted data has 23972 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = budget_food(test_path)
  try:
    assert x_train.shape == (23972, 6)
  except:
    shutil.rmtree(test_path)
    raise()
