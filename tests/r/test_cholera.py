from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cholera import cholera


def test_cholera():
  """Test module cholera.py by downloading
   cholera.csv and testing shape of
   extracted data has 38 rows and 15 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cholera(test_path)
  try:
    assert x_train.shape == (38, 15)
  except:
    shutil.rmtree(test_path)
    raise()
