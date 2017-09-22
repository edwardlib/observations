from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.geyser import geyser


def test_geyser():
  """Test module geyser.py by downloading
   geyser.csv and testing shape of
   extracted data has 299 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = geyser(test_path)
  try:
    assert x_train.shape == (299, 2)
  except:
    shutil.rmtree(test_path)
    raise()
