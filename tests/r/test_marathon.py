from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.marathon import marathon


def test_marathon():
  """Test module marathon.py by downloading
   marathon.csv and testing shape of
   extracted data has 1127 rows and 9 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = marathon(test_path)
  try:
    assert x_train.shape == (1127, 9)
  except:
    shutil.rmtree(test_path)
    raise()
