from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.beveridge import beveridge


def test_beveridge():
  """Test module beveridge.py by downloading
   beveridge.csv and testing shape of
   extracted data has 135 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = beveridge(test_path)
  try:
    assert x_train.shape == (135, 8)
  except:
    shutil.rmtree(test_path)
    raise()
