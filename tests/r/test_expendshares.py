from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.expendshares import expendshares


def test_expendshares():
  """Test module expendshares.py by downloading
   expendshares.csv and testing shape of
   extracted data has 1519 rows and 13 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = expendshares(test_path)
  try:
    assert x_train.shape == (1519, 13)
  except:
    shutil.rmtree(test_path)
    raise()
