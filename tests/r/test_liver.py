from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.liver import liver


def test_liver():
  """Test module liver.py by downloading
   liver.csv and testing shape of
   extracted data has 606 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = liver(test_path)
  try:
    assert x_train.shape == (606, 9)
  except:
    shutil.rmtree(test_path)
    raise()
