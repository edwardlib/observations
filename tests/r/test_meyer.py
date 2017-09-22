from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.meyer import meyer


def test_meyer():
  """Test module meyer.py by downloading
   meyer.csv and testing shape of
   extracted data has 306 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = meyer(test_path)
  try:
    assert x_train.shape == (306, 5)
  except:
    shutil.rmtree(test_path)
    raise()
