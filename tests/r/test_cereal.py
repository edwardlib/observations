from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cereal import cereal


def test_cereal():
  """Test module cereal.py by downloading
   cereal.csv and testing shape of
   extracted data has 36 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cereal(test_path)
  try:
    assert x_train.shape == (36, 4)
  except:
    shutil.rmtree(test_path)
    raise()
