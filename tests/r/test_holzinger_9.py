from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.holzinger_9 import holzinger_9


def test_holzinger_9():
  """Test module holzinger_9.py by downloading
   holzinger_9.csv and testing shape of
   extracted data has 9 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = holzinger_9(test_path)
  try:
    assert x_train.shape == (9, 9)
  except:
    shutil.rmtree(test_path)
    raise()
