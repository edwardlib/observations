from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.xclara import xclara


def test_xclara():
  """Test module xclara.py by downloading
   xclara.csv and testing shape of
   extracted data has 3000 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = xclara(test_path)
  try:
    assert x_train.shape == (3000, 2)
  except:
    shutil.rmtree(test_path)
    raise()
