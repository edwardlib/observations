from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.coalition import coalition


def test_coalition():
  """Test module coalition.py by downloading
   coalition.csv and testing shape of
   extracted data has 314 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = coalition(test_path)
  try:
    assert x_train.shape == (314, 7)
  except:
    shutil.rmtree(test_path)
    raise()
