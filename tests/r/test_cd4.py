from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cd4 import cd4


def test_cd4():
  """Test module cd4.py by downloading
   cd4.csv and testing shape of
   extracted data has 20 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cd4(test_path)
  try:
    assert x_train.shape == (20, 2)
  except:
    shutil.rmtree(test_path)
    raise()
