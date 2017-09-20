from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.vlt import vlt


def test_vlt():
  """Test module vlt.py by downloading
   vlt.csv and testing shape of
   extracted data has 345 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = vlt(test_path)
  try:
    assert x_train.shape == (345, 5)
  except:
    shutil.rmtree(test_path)
    raise()
