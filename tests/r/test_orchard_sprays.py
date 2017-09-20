from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.orchard_sprays import orchard_sprays


def test_orchard_sprays():
  """Test module orchard_sprays.py by downloading
   orchard_sprays.csv and testing shape of
   extracted data has 64 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = orchard_sprays(test_path)
  try:
    assert x_train.shape == (64, 4)
  except:
    shutil.rmtree(test_path)
    raise()
