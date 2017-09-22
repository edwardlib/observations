from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.budget_italy import budget_italy


def test_budget_italy():
  """Test module budget_italy.py by downloading
   budget_italy.csv and testing shape of
   extracted data has 1729 rows and 11 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = budget_italy(test_path)
  try:
    assert x_train.shape == (1729, 11)
  except:
    shutil.rmtree(test_path)
    raise()
