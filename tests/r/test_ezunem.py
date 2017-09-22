from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ezunem import ezunem


def test_ezunem():
  """Test module ezunem.py by downloading
   ezunem.csv and testing shape of
   extracted data has 198 rows and 37 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ezunem(test_path)
  try:
    assert x_train.shape == (198, 37)
  except:
    shutil.rmtree(test_path)
    raise()
