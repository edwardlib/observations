from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.flchain import flchain


def test_flchain():
  """Test module flchain.py by downloading
   flchain.csv and testing shape of
   extracted data has 7874 rows and 11 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = flchain(test_path)
  try:
    assert x_train.shape == (7874, 11)
  except:
    shutil.rmtree(test_path)
    raise()
