from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.chickwts import chickwts


def test_chickwts():
  """Test module chickwts.py by downloading
   chickwts.csv and testing shape of
   extracted data has 71 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = chickwts(test_path)
  try:
    assert x_train.shape == (71, 2)
  except:
    shutil.rmtree(test_path)
    raise()
