from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.colon import colon


def test_colon():
  """Test module colon.py by downloading
   colon.csv and testing shape of
   extracted data has 1858 rows and 16 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = colon(test_path)
  try:
    assert x_train.shape == (1858, 16)
  except:
    shutil.rmtree(test_path)
    raise()
