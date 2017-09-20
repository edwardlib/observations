from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.rearrests import rearrests


def test_rearrests():
  """Test module rearrests.py by downloading
   rearrests.csv and testing shape of
   extracted data has 2 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = rearrests(test_path)
  try:
    assert x_train.shape == (2, 2)
  except:
    shutil.rmtree(test_path)
    raise()
