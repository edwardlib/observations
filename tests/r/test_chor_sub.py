from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.chor_sub import chor_sub


def test_chor_sub():
  """Test module chor_sub.py by downloading
   chor_sub.csv and testing shape of
   extracted data has 61 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = chor_sub(test_path)
  try:
    assert x_train.shape == (61, 10)
  except:
    shutil.rmtree(test_path)
    raise()
