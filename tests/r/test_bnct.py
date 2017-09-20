from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bnct import bnct


def test_bnct():
  """Test module bnct.py by downloading
   bnct.csv and testing shape of
   extracted data has 30 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bnct(test_path)
  try:
    assert x_train.shape == (30, 3)
  except:
    shutil.rmtree(test_path)
    raise()
