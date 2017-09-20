from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.forbes2000 import forbes2000


def test_forbes2000():
  """Test module forbes2000.py by downloading
   forbes2000.csv and testing shape of
   extracted data has 2000 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = forbes2000(test_path)
  try:
    assert x_train.shape == (2000, 8)
  except:
    shutil.rmtree(test_path)
    raise()
