from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.dactyl import dactyl


def test_dactyl():
  """Test module dactyl.py by downloading
   dactyl.csv and testing shape of
   extracted data has 60 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = dactyl(test_path)
  try:
    assert x_train.shape == (60, 3)
  except:
    shutil.rmtree(test_path)
    raise()
