from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.pottery import pottery


def test_pottery():
  """Test module pottery.py by downloading
   pottery.csv and testing shape of
   extracted data has 26 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = pottery(test_path)
  try:
    assert x_train.shape == (26, 6)
  except:
    shutil.rmtree(test_path)
    raise()
