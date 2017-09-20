from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.rotifer import rotifer


def test_rotifer():
  """Test module rotifer.py by downloading
   rotifer.csv and testing shape of
   extracted data has 20 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = rotifer(test_path)
  try:
    assert x_train.shape == (20, 5)
  except:
    shutil.rmtree(test_path)
    raise()
