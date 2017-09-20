from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.eidat import eidat


def test_eidat():
  """Test module eidat.py by downloading
   eidat.csv and testing shape of
   extracted data has 10 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = eidat(test_path)
  try:
    assert x_train.shape == (10, 4)
  except:
    shutil.rmtree(test_path)
    raise()
