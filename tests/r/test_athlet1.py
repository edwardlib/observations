from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.athlet1 import athlet1


def test_athlet1():
  """Test module athlet1.py by downloading
   athlet1.csv and testing shape of
   extracted data has 118 rows and 23 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = athlet1(test_path)
  try:
    assert x_train.shape == (118, 23)
  except:
    shutil.rmtree(test_path)
    raise()
