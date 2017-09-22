from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cowles import cowles


def test_cowles():
  """Test module cowles.py by downloading
   cowles.csv and testing shape of
   extracted data has 1421 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cowles(test_path)
  try:
    assert x_train.shape == (1421, 4)
  except:
    shutil.rmtree(test_path)
    raise()
