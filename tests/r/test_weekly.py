from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.weekly import weekly


def test_weekly():
  """Test module weekly.py by downloading
   weekly.csv and testing shape of
   extracted data has 1089 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = weekly(test_path)
  try:
    assert x_train.shape == (1089, 9)
  except:
    shutil.rmtree(test_path)
    raise()
