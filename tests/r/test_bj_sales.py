from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bj_sales import bj_sales


def test_bj_sales():
  """Test module bj_sales.py by downloading
   bj_sales.csv and testing shape of
   extracted data has 150 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bj_sales(test_path)
  try:
    assert x_train.shape == (150, 2)
  except:
    shutil.rmtree(test_path)
    raise()
