from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.leaftemp import leaftemp


def test_leaftemp():
  """Test module leaftemp.py by downloading
   leaftemp.csv and testing shape of
   extracted data has 62 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = leaftemp(test_path)
  try:
    assert x_train.shape == (62, 4)
  except:
    shutil.rmtree(test_path)
    raise()
