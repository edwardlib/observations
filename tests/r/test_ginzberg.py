from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ginzberg import ginzberg


def test_ginzberg():
  """Test module ginzberg.py by downloading
   ginzberg.csv and testing shape of
   extracted data has 82 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ginzberg(test_path)
  try:
    assert x_train.shape == (82, 6)
  except:
    shutil.rmtree(test_path)
    raise()
