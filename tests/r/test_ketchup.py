from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ketchup import ketchup


def test_ketchup():
  """Test module ketchup.py by downloading
   ketchup.csv and testing shape of
   extracted data has 4956 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ketchup(test_path)
  try:
    assert x_train.shape == (4956, 7)
  except:
    shutil.rmtree(test_path)
    raise()
