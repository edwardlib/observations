from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.swiss import swiss


def test_swiss():
  """Test module swiss.py by downloading
   swiss.csv and testing shape of
   extracted data has 47 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = swiss(test_path)
  try:
    assert x_train.shape == (47, 6)
  except:
    shutil.rmtree(test_path)
    raise()
