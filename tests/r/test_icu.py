from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.icu import icu


def test_icu():
  """Test module icu.py by downloading
   icu.csv and testing shape of
   extracted data has 200 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = icu(test_path)
  try:
    assert x_train.shape == (200, 9)
  except:
    shutil.rmtree(test_path)
    raise()
