from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.pre_sex import pre_sex


def test_pre_sex():
  """Test module pre_sex.py by downloading
   pre_sex.csv and testing shape of
   extracted data has 16 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = pre_sex(test_path)
  try:
    assert x_train.shape == (16, 5)
  except:
    shutil.rmtree(test_path)
    raise()
