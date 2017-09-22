from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.blue_jays import blue_jays


def test_blue_jays():
  """Test module blue_jays.py by downloading
   blue_jays.csv and testing shape of
   extracted data has 123 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = blue_jays(test_path)
  try:
    assert x_train.shape == (123, 9)
  except:
    shutil.rmtree(test_path)
    raise()
