from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cvalues import cvalues


def test_cvalues():
  """Test module cvalues.py by downloading
   cvalues.csv and testing shape of
   extracted data has 9 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cvalues(test_path)
  try:
    assert x_train.shape == (9, 3)
  except:
    shutil.rmtree(test_path)
    raise()
