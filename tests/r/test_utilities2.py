from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.utilities2 import utilities2


def test_utilities2():
  """Test module utilities2.py by downloading
   utilities2.csv and testing shape of
   extracted data has 117 rows and 19 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = utilities2(test_path)
  try:
    assert x_train.shape == (117, 19)
  except:
    shutil.rmtree(test_path)
    raise()
