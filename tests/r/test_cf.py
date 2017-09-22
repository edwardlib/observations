from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cf import cf


def test_cf():
  """Test module cf.py by downloading
   cf.csv and testing shape of
   extracted data has 186 rows and 24 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cf(test_path)
  try:
    assert x_train.shape == (186, 24)
  except:
    shutil.rmtree(test_path)
    raise()
