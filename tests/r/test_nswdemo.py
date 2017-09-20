from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.nswdemo import nswdemo


def test_nswdemo():
  """Test module nswdemo.py by downloading
   nswdemo.csv and testing shape of
   extracted data has 722 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = nswdemo(test_path)
  try:
    assert x_train.shape == (722, 10)
  except:
    shutil.rmtree(test_path)
    raise()
