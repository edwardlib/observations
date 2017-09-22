from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.wong import wong


def test_wong():
  """Test module wong.py by downloading
   wong.csv and testing shape of
   extracted data has 331 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = wong(test_path)
  try:
    assert x_train.shape == (331, 7)
  except:
    shutil.rmtree(test_path)
    raise()
