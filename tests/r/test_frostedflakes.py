from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.frostedflakes import frostedflakes


def test_frostedflakes():
  """Test module frostedflakes.py by downloading
   frostedflakes.csv and testing shape of
   extracted data has 100 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = frostedflakes(test_path)
  try:
    assert x_train.shape == (100, 2)
  except:
    shutil.rmtree(test_path)
    raise()
