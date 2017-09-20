from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.boston import boston


def test_boston():
  """Test module boston.py by downloading
   boston.csv and testing shape of
   extracted data has 506 rows and 14 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = boston(test_path)
  try:
    assert x_train.shape == (506, 14)
  except:
    shutil.rmtree(test_path)
    raise()
