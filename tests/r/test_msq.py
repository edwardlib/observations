from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.msq import msq


def test_msq():
  """Test module msq.py by downloading
   msq.csv and testing shape of
   extracted data has 3896 rows and 92 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = msq(test_path)
  try:
    assert x_train.shape == (3896, 92)
  except:
    shutil.rmtree(test_path)
    raise()
