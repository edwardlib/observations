from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.l51 import l51


def test_l51():
  """Test module l51.py by downloading
   l51.csv and testing shape of
   extracted data has 51 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = l51(test_path)
  try:
    assert x_train.shape == (51, 6)
  except:
    shutil.rmtree(test_path)
    raise()
