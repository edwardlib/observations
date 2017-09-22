from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.mandel import mandel


def test_mandel():
  """Test module mandel.py by downloading
   mandel.csv and testing shape of
   extracted data has 8 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = mandel(test_path)
  try:
    assert x_train.shape == (8, 3)
  except:
    shutil.rmtree(test_path)
    raise()
