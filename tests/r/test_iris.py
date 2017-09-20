from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.iris import iris


def test_iris():
  """Test module iris.py by downloading
   iris.csv and testing shape of
   extracted data has 150 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = iris(test_path)
  try:
    assert x_train.shape == (150, 5)
  except:
    shutil.rmtree(test_path)
    raise()
