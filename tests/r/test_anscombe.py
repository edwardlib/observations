from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.anscombe import anscombe


def test_anscombe():
  """Test module anscombe.py by downloading
   anscombe.csv and testing shape of
   extracted data has 11 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = anscombe(test_path)
  try:
    assert x_train.shape == (11, 8)
  except:
    shutil.rmtree(test_path)
    raise()
