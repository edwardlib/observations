from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.breaches import breaches


def test_breaches():
  """Test module breaches.py by downloading
   breaches.csv and testing shape of
   extracted data has 1055 rows and 13 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = breaches(test_path)
  try:
    assert x_train.shape == (1055, 13)
  except:
    shutil.rmtree(test_path)
    raise()
