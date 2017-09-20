from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.aids import aids


def test_aids():
  """Test module aids.py by downloading
   aids.csv and testing shape of
   extracted data has 295 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = aids(test_path)
  try:
    assert x_train.shape == (295, 3)
  except:
    shutil.rmtree(test_path)
    raise()
