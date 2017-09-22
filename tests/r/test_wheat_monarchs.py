from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.wheat_monarchs import wheat_monarchs


def test_wheat_monarchs():
  """Test module wheat_monarchs.py by downloading
   wheat_monarchs.csv and testing shape of
   extracted data has 12 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = wheat_monarchs(test_path)
  try:
    assert x_train.shape == (12, 4)
  except:
    shutil.rmtree(test_path)
    raise()
