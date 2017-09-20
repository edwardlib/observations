from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.yeast import yeast


def test_yeast():
  """Test module yeast.py by downloading
   yeast.csv and testing shape of
   extracted data has 36 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = yeast(test_path)
  try:
    assert x_train.shape == (36, 3)
  except:
    shutil.rmtree(test_path)
    raise()
