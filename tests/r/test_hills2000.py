from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.hills2000 import hills2000


def test_hills2000():
  """Test module hills2000.py by downloading
   hills2000.csv and testing shape of
   extracted data has 56 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = hills2000(test_path)
  try:
    assert x_train.shape == (56, 4)
  except:
    shutil.rmtree(test_path)
    raise()
