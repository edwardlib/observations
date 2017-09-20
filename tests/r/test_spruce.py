from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.spruce import spruce


def test_spruce():
  """Test module spruce.py by downloading
   spruce.csv and testing shape of
   extracted data has 1027 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = spruce(test_path)
  try:
    assert x_train.shape == (1027, 6)
  except:
    shutil.rmtree(test_path)
    raise()
