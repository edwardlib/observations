from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.manitoba_lakes import manitoba_lakes


def test_manitoba_lakes():
  """Test module manitoba_lakes.py by downloading
   manitoba_lakes.csv and testing shape of
   extracted data has 9 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = manitoba_lakes(test_path)
  try:
    assert x_train.shape == (9, 2)
  except:
    shutil.rmtree(test_path)
    raise()
