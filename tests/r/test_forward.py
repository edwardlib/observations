from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.forward import forward


def test_forward():
  """Test module forward.py by downloading
   forward.csv and testing shape of
   extracted data has 276 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = forward(test_path)
  try:
    assert x_train.shape == (276, 9)
  except:
    shutil.rmtree(test_path)
    raise()
