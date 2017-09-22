from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.wages1833 import wages1833


def test_wages1833():
  """Test module wages1833.py by downloading
   wages1833.csv and testing shape of
   extracted data has 51 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = wages1833(test_path)
  try:
    assert x_train.shape == (51, 5)
  except:
    shutil.rmtree(test_path)
    raise()
