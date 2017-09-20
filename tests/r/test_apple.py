from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.apple import apple


def test_apple():
  """Test module apple.py by downloading
   apple.csv and testing shape of
   extracted data has 660 rows and 17 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = apple(test_path)
  try:
    assert x_train.shape == (660, 17)
  except:
    shutil.rmtree(test_path)
    raise()
