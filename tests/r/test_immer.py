from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.immer import immer


def test_immer():
  """Test module immer.py by downloading
   immer.csv and testing shape of
   extracted data has 30 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = immer(test_path)
  try:
    assert x_train.shape == (30, 4)
  except:
    shutil.rmtree(test_path)
    raise()
