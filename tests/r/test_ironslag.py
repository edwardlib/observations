from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ironslag import ironslag


def test_ironslag():
  """Test module ironslag.py by downloading
   ironslag.csv and testing shape of
   extracted data has 53 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ironslag(test_path)
  try:
    assert x_train.shape == (53, 2)
  except:
    shutil.rmtree(test_path)
    raise()
