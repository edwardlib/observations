from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.titanicgrp import titanicgrp


def test_titanicgrp():
  """Test module titanicgrp.py by downloading
   titanicgrp.csv and testing shape of
   extracted data has 12 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = titanicgrp(test_path)
  try:
    assert x_train.shape == (12, 5)
  except:
    shutil.rmtree(test_path)
    raise()
