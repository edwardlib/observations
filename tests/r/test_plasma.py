from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.plasma import plasma


def test_plasma():
  """Test module plasma.py by downloading
   plasma.csv and testing shape of
   extracted data has 32 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = plasma(test_path)
  try:
    assert x_train.shape == (32, 3)
  except:
    shutil.rmtree(test_path)
    raise()
