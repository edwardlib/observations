from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.rwm import rwm


def test_rwm():
  """Test module rwm.py by downloading
   rwm.csv and testing shape of
   extracted data has 27326 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = rwm(test_path)
  try:
    assert x_train.shape == (27326, 4)
  except:
    shutil.rmtree(test_path)
    raise()
