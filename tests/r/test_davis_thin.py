from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.davis_thin import davis_thin


def test_davis_thin():
  """Test module davis_thin.py by downloading
   davis_thin.csv and testing shape of
   extracted data has 191 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = davis_thin(test_path)
  try:
    assert x_train.shape == (191, 7)
  except:
    shutil.rmtree(test_path)
    raise()
