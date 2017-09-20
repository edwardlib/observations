from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.std import std


def test_std():
  """Test module std.py by downloading
   std.csv and testing shape of
   extracted data has 877 rows and 24 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = std(test_path)
  try:
    assert x_train.shape == (877, 24)
  except:
    shutil.rmtree(test_path)
    raise()
