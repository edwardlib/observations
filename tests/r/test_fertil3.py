from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.fertil3 import fertil3


def test_fertil3():
  """Test module fertil3.py by downloading
   fertil3.csv and testing shape of
   extracted data has 72 rows and 24 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = fertil3(test_path)
  try:
    assert x_train.shape == (72, 24)
  except:
    shutil.rmtree(test_path)
    raise()
