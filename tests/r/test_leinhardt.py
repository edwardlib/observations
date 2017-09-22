from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.leinhardt import leinhardt


def test_leinhardt():
  """Test module leinhardt.py by downloading
   leinhardt.csv and testing shape of
   extracted data has 105 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = leinhardt(test_path)
  try:
    assert x_train.shape == (105, 4)
  except:
    shutil.rmtree(test_path)
    raise()
