from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.yen import yen


def test_yen():
  """Test module yen.py by downloading
   yen.csv and testing shape of
   extracted data has 778 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = yen(test_path)
  try:
    assert x_train.shape == (778, 4)
  except:
    shutil.rmtree(test_path)
    raise()
