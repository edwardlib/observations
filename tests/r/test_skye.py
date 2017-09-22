from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.skye import skye


def test_skye():
  """Test module skye.py by downloading
   skye.csv and testing shape of
   extracted data has 23 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = skye(test_path)
  try:
    assert x_train.shape == (23, 3)
  except:
    shutil.rmtree(test_path)
    raise()
