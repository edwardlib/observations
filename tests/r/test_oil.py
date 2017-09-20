from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.oil import oil


def test_oil():
  """Test module oil.py by downloading
   oil.csv and testing shape of
   extracted data has 53 rows and 11 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = oil(test_path)
  try:
    assert x_train.shape == (53, 11)
  except:
    shutil.rmtree(test_path)
    raise()
