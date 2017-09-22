from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.rice_farms import rice_farms


def test_rice_farms():
  """Test module rice_farms.py by downloading
   rice_farms.csv and testing shape of
   extracted data has 1026 rows and 20 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = rice_farms(test_path)
  try:
    assert x_train.shape == (1026, 20)
  except:
    shutil.rmtree(test_path)
    raise()
