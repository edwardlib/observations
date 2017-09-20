from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.telef import telef


def test_telef():
  """Test module telef.py by downloading
   telef.csv and testing shape of
   extracted data has 24 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = telef(test_path)
  try:
    assert x_train.shape == (24, 2)
  except:
    shutil.rmtree(test_path)
    raise()
