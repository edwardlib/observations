from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.nidd import nidd


def test_nidd():
  """Test module nidd.py by downloading
   nidd.csv and testing shape of
   extracted data has 154 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = nidd(test_path)
  try:
    assert x_train.shape == (154, 1)
  except:
    shutil.rmtree(test_path)
    raise()
