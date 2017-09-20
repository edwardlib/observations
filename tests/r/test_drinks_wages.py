from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.drinks_wages import drinks_wages


def test_drinks_wages():
  """Test module drinks_wages.py by downloading
   drinks_wages.csv and testing shape of
   extracted data has 70 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = drinks_wages(test_path)
  try:
    assert x_train.shape == (70, 6)
  except:
    shutil.rmtree(test_path)
    raise()
