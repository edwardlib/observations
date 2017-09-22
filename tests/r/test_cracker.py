from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cracker import cracker


def test_cracker():
  """Test module cracker.py by downloading
   cracker.csv and testing shape of
   extracted data has 3292 rows and 14 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cracker(test_path)
  try:
    assert x_train.shape == (3292, 14)
  except:
    shutil.rmtree(test_path)
    raise()
