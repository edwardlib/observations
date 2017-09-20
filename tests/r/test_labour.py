from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.labour import labour


def test_labour():
  """Test module labour.py by downloading
   labour.csv and testing shape of
   extracted data has 569 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = labour(test_path)
  try:
    assert x_train.shape == (569, 4)
  except:
    shutil.rmtree(test_path)
    raise()
