from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.slp75_81 import slp75_81


def test_slp75_81():
  """Test module slp75_81.py by downloading
   slp75_81.csv and testing shape of
   extracted data has 239 rows and 20 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = slp75_81(test_path)
  try:
    assert x_train.shape == (239, 20)
  except:
    shutil.rmtree(test_path)
    raise()
