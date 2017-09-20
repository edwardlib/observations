from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.thurstone_33 import thurstone_33


def test_thurstone_33():
  """Test module thurstone_33.py by downloading
   thurstone_33.csv and testing shape of
   extracted data has 9 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = thurstone_33(test_path)
  try:
    assert x_train.shape == (9, 9)
  except:
    shutil.rmtree(test_path)
    raise()
