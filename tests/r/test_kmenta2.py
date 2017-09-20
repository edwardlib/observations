from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.kmenta2 import kmenta2


def test_kmenta2():
  """Test module kmenta2.py by downloading
   kmenta2.csv and testing shape of
   extracted data has 20 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = kmenta2(test_path)
  try:
    assert x_train.shape == (20, 5)
  except:
    shutil.rmtree(test_path)
    raise()
