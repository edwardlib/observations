from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ais import ais


def test_ais():
  """Test module ais.py by downloading
   ais.csv and testing shape of
   extracted data has 202 rows and 13 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ais(test_path)
  try:
    assert x_train.shape == (202, 13)
  except:
    shutil.rmtree(test_path)
    raise()
