from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.caith import caith


def test_caith():
  """Test module caith.py by downloading
   caith.csv and testing shape of
   extracted data has 4 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = caith(test_path)
  try:
    assert x_train.shape == (4, 5)
  except:
    shutil.rmtree(test_path)
    raise()
