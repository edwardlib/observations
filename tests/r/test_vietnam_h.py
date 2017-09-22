from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.vietnam_h import vietnam_h


def test_vietnam_h():
  """Test module vietnam_h.py by downloading
   vietnam_h.csv and testing shape of
   extracted data has 5999 rows and 11 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = vietnam_h(test_path)
  try:
    assert x_train.shape == (5999, 11)
  except:
    shutil.rmtree(test_path)
    raise()
