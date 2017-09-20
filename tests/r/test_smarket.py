from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.smarket import smarket


def test_smarket():
  """Test module smarket.py by downloading
   smarket.csv and testing shape of
   extracted data has 1250 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = smarket(test_path)
  try:
    assert x_train.shape == (1250, 9)
  except:
    shutil.rmtree(test_path)
    raise()
