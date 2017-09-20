from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.klein2 import klein2


def test_klein2():
  """Test module klein2.py by downloading
   klein2.csv and testing shape of
   extracted data has 21 rows and 14 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = klein2(test_path)
  try:
    assert x_train.shape == (21, 14)
  except:
    shutil.rmtree(test_path)
    raise()
