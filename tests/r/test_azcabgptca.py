from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.azcabgptca import azcabgptca


def test_azcabgptca():
  """Test module azcabgptca.py by downloading
   azcabgptca.csv and testing shape of
   extracted data has 1959 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = azcabgptca(test_path)
  try:
    assert x_train.shape == (1959, 6)
  except:
    shutil.rmtree(test_path)
    raise()
