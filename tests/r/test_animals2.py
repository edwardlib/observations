from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.animals2 import animals2


def test_animals2():
  """Test module animals2.py by downloading
   animals2.csv and testing shape of
   extracted data has 65 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = animals2(test_path)
  try:
    assert x_train.shape == (65, 2)
  except:
    shutil.rmtree(test_path)
    raise()
