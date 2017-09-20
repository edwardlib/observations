from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.fruit_flies import fruit_flies


def test_fruit_flies():
  """Test module fruit_flies.py by downloading
   fruit_flies.csv and testing shape of
   extracted data has 125 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = fruit_flies(test_path)
  try:
    assert x_train.shape == (125, 7)
  except:
    shutil.rmtree(test_path)
    raise()
