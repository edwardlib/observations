from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ruspini import ruspini


def test_ruspini():
  """Test module ruspini.py by downloading
   ruspini.csv and testing shape of
   extracted data has 75 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ruspini(test_path)
  try:
    assert x_train.shape == (75, 2)
  except:
    shutil.rmtree(test_path)
    raise()
