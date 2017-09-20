from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.pig_feed import pig_feed


def test_pig_feed():
  """Test module pig_feed.py by downloading
   pig_feed.csv and testing shape of
   extracted data has 12 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = pig_feed(test_path)
  try:
    assert x_train.shape == (12, 3)
  except:
    shutil.rmtree(test_path)
    raise()
