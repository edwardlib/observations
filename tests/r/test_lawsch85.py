from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.lawsch85 import lawsch85


def test_lawsch85():
  """Test module lawsch85.py by downloading
   lawsch85.csv and testing shape of
   extracted data has 156 rows and 21 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = lawsch85(test_path)
  try:
    assert x_train.shape == (156, 21)
  except:
    shutil.rmtree(test_path)
    raise()
