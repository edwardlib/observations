from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cottonworkers import cottonworkers


def test_cottonworkers():
  """Test module cottonworkers.py by downloading
   cottonworkers.csv and testing shape of
   extracted data has 14 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cottonworkers(test_path)
  try:
    assert x_train.shape == (14, 3)
  except:
    shutil.rmtree(test_path)
    raise()
