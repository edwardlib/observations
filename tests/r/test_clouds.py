from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.clouds import clouds


def test_clouds():
  """Test module clouds.py by downloading
   clouds.csv and testing shape of
   extracted data has 24 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = clouds(test_path)
  try:
    assert x_train.shape == (24, 7)
  except:
    shutil.rmtree(test_path)
    raise()
