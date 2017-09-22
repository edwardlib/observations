from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.azdrg112 import azdrg112


def test_azdrg112():
  """Test module azdrg112.py by downloading
   azdrg112.csv and testing shape of
   extracted data has 1798 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = azdrg112(test_path)
  try:
    assert x_train.shape == (1798, 4)
  except:
    shutil.rmtree(test_path)
    raise()
