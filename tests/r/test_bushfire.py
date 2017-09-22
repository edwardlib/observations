from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bushfire import bushfire


def test_bushfire():
  """Test module bushfire.py by downloading
   bushfire.csv and testing shape of
   extracted data has 38 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bushfire(test_path)
  try:
    assert x_train.shape == (38, 5)
  except:
    shutil.rmtree(test_path)
    raise()
