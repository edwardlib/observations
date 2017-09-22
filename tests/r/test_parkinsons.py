from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.parkinsons import parkinsons


def test_parkinsons():
  """Test module parkinsons.py by downloading
   parkinsons.csv and testing shape of
   extracted data has 825 rows and 22 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = parkinsons(test_path)
  try:
    assert x_train.shape == (825, 22)
  except:
    shutil.rmtree(test_path)
    raise()
