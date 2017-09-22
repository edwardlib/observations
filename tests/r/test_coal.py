from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.coal import coal


def test_coal():
  """Test module coal.py by downloading
   coal.csv and testing shape of
   extracted data has 191 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = coal(test_path)
  try:
    assert x_train.shape == (191, 1)
  except:
    shutil.rmtree(test_path)
    raise()
