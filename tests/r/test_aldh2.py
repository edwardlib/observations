from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.aldh2 import aldh2


def test_aldh2():
  """Test module aldh2.py by downloading
   aldh2.csv and testing shape of
   extracted data has 263 rows and 18 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = aldh2(test_path)
  try:
    assert x_train.shape == (263, 18)
  except:
    shutil.rmtree(test_path)
    raise()
