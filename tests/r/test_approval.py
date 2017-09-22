from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.approval import approval


def test_approval():
  """Test module approval.py by downloading
   approval.csv and testing shape of
   extracted data has 65 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = approval(test_path)
  try:
    assert x_train.shape == (65, 8)
  except:
    shutil.rmtree(test_path)
    raise()
