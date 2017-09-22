from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.gasoline import gasoline


def test_gasoline():
  """Test module gasoline.py by downloading
   gasoline.csv and testing shape of
   extracted data has 342 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = gasoline(test_path)
  try:
    assert x_train.shape == (342, 6)
  except:
    shutil.rmtree(test_path)
    raise()
