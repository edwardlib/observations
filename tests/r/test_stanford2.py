from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.stanford2 import stanford2


def test_stanford2():
  """Test module stanford2.py by downloading
   stanford2.csv and testing shape of
   extracted data has 184 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = stanford2(test_path)
  try:
    assert x_train.shape == (184, 5)
  except:
    shutil.rmtree(test_path)
    raise()
