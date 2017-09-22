from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.minard_cities import minard_cities


def test_minard_cities():
  """Test module minard_cities.py by downloading
   minard_cities.csv and testing shape of
   extracted data has 20 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = minard_cities(test_path)
  try:
    assert x_train.shape == (20, 3)
  except:
    shutil.rmtree(test_path)
    raise()
