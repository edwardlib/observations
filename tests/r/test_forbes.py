from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.forbes import forbes


def test_forbes():
  """Test module forbes.py by downloading
   forbes.csv and testing shape of
   extracted data has 17 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = forbes(test_path)
  try:
    assert x_train.shape == (17, 2)
  except:
    shutil.rmtree(test_path)
    raise()
