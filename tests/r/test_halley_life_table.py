from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.halley_life_table import halley_life_table


def test_halley_life_table():
  """Test module halley_life_table.py by downloading
   halley_life_table.csv and testing shape of
   extracted data has 84 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = halley_life_table(test_path)
  try:
    assert x_train.shape == (84, 4)
  except:
    shutil.rmtree(test_path)
    raise()
