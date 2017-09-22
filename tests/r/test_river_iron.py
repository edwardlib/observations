from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.river_iron import river_iron


def test_river_iron():
  """Test module river_iron.py by downloading
   river_iron.csv and testing shape of
   extracted data has 12 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = river_iron(test_path)
  try:
    assert x_train.shape == (12, 4)
  except:
    shutil.rmtree(test_path)
    raise()
