from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.solder import solder


def test_solder():
  """Test module solder.py by downloading
   solder.csv and testing shape of
   extracted data has 720 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = solder(test_path)
  try:
    assert x_train.shape == (720, 6)
  except:
    shutil.rmtree(test_path)
    raise()
