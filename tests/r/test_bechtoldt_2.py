from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bechtoldt_2 import bechtoldt_2


def test_bechtoldt_2():
  """Test module bechtoldt_2.py by downloading
   bechtoldt_2.csv and testing shape of
   extracted data has 17 rows and 17 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bechtoldt_2(test_path)
  try:
    assert x_train.shape == (17, 17)
  except:
    shutil.rmtree(test_path)
    raise()
