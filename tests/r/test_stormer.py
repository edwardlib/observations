from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.stormer import stormer


def test_stormer():
  """Test module stormer.py by downloading
   stormer.csv and testing shape of
   extracted data has 23 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = stormer(test_path)
  try:
    assert x_train.shape == (23, 3)
  except:
    shutil.rmtree(test_path)
    raise()
