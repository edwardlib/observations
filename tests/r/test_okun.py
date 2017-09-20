from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.okun import okun


def test_okun():
  """Test module okun.py by downloading
   okun.csv and testing shape of
   extracted data has 47 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = okun(test_path)
  try:
    assert x_train.shape == (47, 4)
  except:
    shutil.rmtree(test_path)
    raise()
