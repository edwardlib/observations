from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.rainforest import rainforest


def test_rainforest():
  """Test module rainforest.py by downloading
   rainforest.csv and testing shape of
   extracted data has 65 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = rainforest(test_path)
  try:
    assert x_train.shape == (65, 7)
  except:
    shutil.rmtree(test_path)
    raise()
