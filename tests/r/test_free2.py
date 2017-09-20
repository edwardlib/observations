from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.free2 import free2


def test_free2():
  """Test module free2.py by downloading
   free2.csv and testing shape of
   extracted data has 450 rows and 11 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = free2(test_path)
  try:
    assert x_train.shape == (450, 11)
  except:
    shutil.rmtree(test_path)
    raise()
