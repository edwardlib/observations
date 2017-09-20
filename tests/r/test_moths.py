from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.moths import moths


def test_moths():
  """Test module moths.py by downloading
   moths.csv and testing shape of
   extracted data has 41 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = moths(test_path)
  try:
    assert x_train.shape == (41, 4)
  except:
    shutil.rmtree(test_path)
    raise()
