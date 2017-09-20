from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.heart import heart


def test_heart():
  """Test module heart.py by downloading
   heart.csv and testing shape of
   extracted data has 172 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = heart(test_path)
  try:
    assert x_train.shape == (172, 8)
  except:
    shutil.rmtree(test_path)
    raise()
