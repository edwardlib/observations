from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.nyse import nyse


def test_nyse():
  """Test module nyse.py by downloading
   nyse.csv and testing shape of
   extracted data has 691 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = nyse(test_path)
  try:
    assert x_train.shape == (691, 8)
  except:
    shutil.rmtree(test_path)
    raise()
