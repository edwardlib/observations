from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.lo_bd import lo_bd


def test_lo_bd():
  """Test module lo_bd.py by downloading
   lo_bd.csv and testing shape of
   extracted data has 84 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = lo_bd(test_path)
  try:
    assert x_train.shape == (84, 9)
  except:
    shutil.rmtree(test_path)
    raise()
