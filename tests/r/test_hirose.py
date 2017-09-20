from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.hirose import hirose


def test_hirose():
  """Test module hirose.py by downloading
   hirose.csv and testing shape of
   extracted data has 44 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = hirose(test_path)
  try:
    assert x_train.shape == (44, 3)
  except:
    shutil.rmtree(test_path)
    raise()
