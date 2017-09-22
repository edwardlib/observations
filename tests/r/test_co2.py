from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.co2 import co2


def test_co2():
  """Test module co2.py by downloading
   co2.csv and testing shape of
   extracted data has 237 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = co2(test_path)
  try:
    assert x_train.shape == (237, 2)
  except:
    shutil.rmtree(test_path)
    raise()
