from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.arthritis import arthritis


def test_arthritis():
  """Test module arthritis.py by downloading
   arthritis.csv and testing shape of
   extracted data has 84 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = arthritis(test_path)
  try:
    assert x_train.shape == (84, 5)
  except:
    shutil.rmtree(test_path)
    raise()
