from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.phosphor import phosphor


def test_phosphor():
  """Test module phosphor.py by downloading
   phosphor.csv and testing shape of
   extracted data has 18 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = phosphor(test_path)
  try:
    assert x_train.shape == (18, 3)
  except:
    shutil.rmtree(test_path)
    raise()
