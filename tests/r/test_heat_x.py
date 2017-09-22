from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.heat_x import heat_x


def test_heat_x():
  """Test module heat_x.py by downloading
   heat_x.csv and testing shape of
   extracted data has 6 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = heat_x(test_path)
  try:
    assert x_train.shape == (6, 7)
  except:
    shutil.rmtree(test_path)
    raise()
