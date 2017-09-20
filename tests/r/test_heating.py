from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.heating import heating


def test_heating():
  """Test module heating.py by downloading
   heating.csv and testing shape of
   extracted data has 900 rows and 21 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = heating(test_path)
  try:
    assert x_train.shape == (900, 21)
  except:
    shutil.rmtree(test_path)
    raise()
