from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.city import city


def test_city():
  """Test module city.py by downloading
   city.csv and testing shape of
   extracted data has 10 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = city(test_path)
  try:
    assert x_train.shape == (10, 2)
  except:
    shutil.rmtree(test_path)
    raise()
