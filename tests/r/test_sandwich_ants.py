from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.sandwich_ants import sandwich_ants


def test_sandwich_ants():
  """Test module sandwich_ants.py by downloading
   sandwich_ants.csv and testing shape of
   extracted data has 48 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = sandwich_ants(test_path)
  try:
    assert x_train.shape == (48, 5)
  except:
    shutil.rmtree(test_path)
    raise()
