from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.tinting import tinting


def test_tinting():
  """Test module tinting.py by downloading
   tinting.csv and testing shape of
   extracted data has 182 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = tinting(test_path)
  try:
    assert x_train.shape == (182, 9)
  except:
    shutil.rmtree(test_path)
    raise()
