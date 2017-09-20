from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.fertil1 import fertil1


def test_fertil1():
  """Test module fertil1.py by downloading
   fertil1.csv and testing shape of
   extracted data has 1129 rows and 27 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = fertil1(test_path)
  try:
    assert x_train.shape == (1129, 27)
  except:
    shutil.rmtree(test_path)
    raise()
