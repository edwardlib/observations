from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cuckoos import cuckoos


def test_cuckoos():
  """Test module cuckoos.py by downloading
   cuckoos.csv and testing shape of
   extracted data has 120 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cuckoos(test_path)
  try:
    assert x_train.shape == (120, 4)
  except:
    shutil.rmtree(test_path)
    raise()
