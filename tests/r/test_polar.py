from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.polar import polar


def test_polar():
  """Test module polar.py by downloading
   polar.csv and testing shape of
   extracted data has 50 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = polar(test_path)
  try:
    assert x_train.shape == (50, 2)
  except:
    shutil.rmtree(test_path)
    raise()
