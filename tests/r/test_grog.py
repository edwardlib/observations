from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.grog import grog


def test_grog():
  """Test module grog.py by downloading
   grog.csv and testing shape of
   extracted data has 18 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = grog(test_path)
  try:
    assert x_train.shape == (18, 5)
  except:
    shutil.rmtree(test_path)
    raise()
