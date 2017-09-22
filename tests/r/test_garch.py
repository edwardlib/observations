from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.garch import garch


def test_garch():
  """Test module garch.py by downloading
   garch.csv and testing shape of
   extracted data has 1867 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = garch(test_path)
  try:
    assert x_train.shape == (1867, 8)
  except:
    shutil.rmtree(test_path)
    raise()
