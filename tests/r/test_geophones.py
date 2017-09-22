from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.geophones import geophones


def test_geophones():
  """Test module geophones.py by downloading
   geophones.csv and testing shape of
   extracted data has 56 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = geophones(test_path)
  try:
    assert x_train.shape == (56, 2)
  except:
    shutil.rmtree(test_path)
    raise()
