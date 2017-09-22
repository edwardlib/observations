from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.meap01 import meap01


def test_meap01():
  """Test module meap01.py by downloading
   meap01.csv and testing shape of
   extracted data has 1823 rows and 11 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = meap01(test_path)
  try:
    assert x_train.shape == (1823, 11)
  except:
    shutil.rmtree(test_path)
    raise()
