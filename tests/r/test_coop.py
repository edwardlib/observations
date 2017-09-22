from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.coop import coop


def test_coop():
  """Test module coop.py by downloading
   coop.csv and testing shape of
   extracted data has 252 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = coop(test_path)
  try:
    assert x_train.shape == (252, 4)
  except:
    shutil.rmtree(test_path)
    raise()
