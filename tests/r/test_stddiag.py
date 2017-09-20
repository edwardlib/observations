from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.stddiag import stddiag


def test_stddiag():
  """Test module stddiag.py by downloading
   stddiag.csv and testing shape of
   extracted data has 25 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = stddiag(test_path)
  try:
    assert x_train.shape == (25, 2)
  except:
    shutil.rmtree(test_path)
    raise()
