from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.kootenay import kootenay


def test_kootenay():
  """Test module kootenay.py by downloading
   kootenay.csv and testing shape of
   extracted data has 13 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = kootenay(test_path)
  try:
    assert x_train.shape == (13, 2)
  except:
    shutil.rmtree(test_path)
    raise()
