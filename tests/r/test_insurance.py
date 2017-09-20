from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.insurance import insurance


def test_insurance():
  """Test module insurance.py by downloading
   insurance.csv and testing shape of
   extracted data has 64 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = insurance(test_path)
  try:
    assert x_train.shape == (64, 5)
  except:
    shutil.rmtree(test_path)
    raise()
