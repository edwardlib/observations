from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.co_transfer import co_transfer


def test_co_transfer():
  """Test module co_transfer.py by downloading
   co_transfer.csv and testing shape of
   extracted data has 7 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = co_transfer(test_path)
  try:
    assert x_train.shape == (7, 2)
  except:
    shutil.rmtree(test_path)
    raise()
