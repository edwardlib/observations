from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.wheat import wheat


def test_wheat():
  """Test module wheat.py by downloading
   wheat.csv and testing shape of
   extracted data has 53 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = wheat(test_path)
  try:
    assert x_train.shape == (53, 3)
  except:
    shutil.rmtree(test_path)
    raise()
