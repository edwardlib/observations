from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.affairs import affairs


def test_affairs():
  """Test module affairs.py by downloading
   affairs.csv and testing shape of
   extracted data has 601 rows and 19 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = affairs(test_path)
  try:
    assert x_train.shape == (601, 19)
  except:
    shutil.rmtree(test_path)
    raise()
