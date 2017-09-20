from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.www_usage import www_usage


def test_www_usage():
  """Test module www_usage.py by downloading
   www_usage.csv and testing shape of
   extracted data has 100 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = www_usage(test_path)
  try:
    assert x_train.shape == (100, 2)
  except:
    shutil.rmtree(test_path)
    raise()
