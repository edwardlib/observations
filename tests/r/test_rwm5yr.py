from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.rwm5yr import rwm5yr


def test_rwm5yr():
  """Test module rwm5yr.py by downloading
   rwm5yr.csv and testing shape of
   extracted data has 19609 rows and 17 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = rwm5yr(test_path)
  try:
    assert x_train.shape == (19609, 17)
  except:
    shutil.rmtree(test_path)
    raise()
