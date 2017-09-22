from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.oj import oj


def test_oj():
  """Test module oj.py by downloading
   oj.csv and testing shape of
   extracted data has 1070 rows and 18 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = oj(test_path)
  try:
    assert x_train.shape == (1070, 18)
  except:
    shutil.rmtree(test_path)
    raise()
