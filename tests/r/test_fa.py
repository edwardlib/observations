from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.fa import fa


def test_fa():
  """Test module fa.py by downloading
   fa.csv and testing shape of
   extracted data has 127 rows and 13 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = fa(test_path)
  try:
    assert x_train.shape == (127, 13)
  except:
    shutil.rmtree(test_path)
    raise()
