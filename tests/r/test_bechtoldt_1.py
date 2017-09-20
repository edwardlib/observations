from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bechtoldt_1 import bechtoldt_1


def test_bechtoldt_1():
  """Test module bechtoldt_1.py by downloading
   bechtoldt_1.csv and testing shape of
   extracted data has 17 rows and 17 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bechtoldt_1(test_path)
  try:
    assert x_train.shape == (17, 17)
  except:
    shutil.rmtree(test_path)
    raise()
