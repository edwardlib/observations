from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.shuttle import shuttle


def test_shuttle():
  """Test module shuttle.py by downloading
   shuttle.csv and testing shape of
   extracted data has 256 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = shuttle(test_path)
  try:
    assert x_train.shape == (256, 7)
  except:
    shutil.rmtree(test_path)
    raise()
