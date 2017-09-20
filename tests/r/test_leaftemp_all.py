from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.leaftemp_all import leaftemp_all


def test_leaftemp_all():
  """Test module leaftemp_all.py by downloading
   leaftemp_all.csv and testing shape of
   extracted data has 62 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = leaftemp_all(test_path)
  try:
    assert x_train.shape == (62, 9)
  except:
    shutil.rmtree(test_path)
    raise()
