from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.uis import uis


def test_uis():
  """Test module uis.py by downloading
   uis.csv and testing shape of
   extracted data has 575 rows and 18 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = uis(test_path)
  try:
    assert x_train.shape == (575, 18)
  except:
    shutil.rmtree(test_path)
    raise()
