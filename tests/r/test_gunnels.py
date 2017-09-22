from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.gunnels import gunnels


def test_gunnels():
  """Test module gunnels.py by downloading
   gunnels.csv and testing shape of
   extracted data has 1592 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = gunnels(test_path)
  try:
    assert x_train.shape == (1592, 10)
  except:
    shutil.rmtree(test_path)
    raise()
