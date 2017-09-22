from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.airmiles import airmiles


def test_airmiles():
  """Test module airmiles.py by downloading
   airmiles.csv and testing shape of
   extracted data has 24 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = airmiles(test_path)
  try:
    assert x_train.shape == (24, 2)
  except:
    shutil.rmtree(test_path)
    raise()
