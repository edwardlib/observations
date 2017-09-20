from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.austpop import austpop


def test_austpop():
  """Test module austpop.py by downloading
   austpop.csv and testing shape of
   extracted data has 9 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = austpop(test_path)
  try:
    assert x_train.shape == (9, 10)
  except:
    shutil.rmtree(test_path)
    raise()
