from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ohio import ohio


def test_ohio():
  """Test module ohio.py by downloading
   ohio.csv and testing shape of
   extracted data has 2148 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ohio(test_path)
  try:
    assert x_train.shape == (2148, 4)
  except:
    shutil.rmtree(test_path)
    raise()
