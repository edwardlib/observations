from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.hodg import hodg


def test_hodg():
  """Test module hodg.py by downloading
   hodg.csv and testing shape of
   extracted data has 43 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = hodg(test_path)
  try:
    assert x_train.shape == (43, 6)
  except:
    shutil.rmtree(test_path)
    raise()
