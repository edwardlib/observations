from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.mode import mode


def test_mode():
  """Test module mode.py by downloading
   mode.csv and testing shape of
   extracted data has 453 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = mode(test_path)
  try:
    assert x_train.shape == (453, 9)
  except:
    shutil.rmtree(test_path)
    raise()
