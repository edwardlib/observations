from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.longley import longley


def test_longley():
  """Test module longley.py by downloading
   longley.csv and testing shape of
   extracted data has 16 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = longley(test_path)
  try:
    assert x_train.shape == (16, 7)
  except:
    shutil.rmtree(test_path)
    raise()
