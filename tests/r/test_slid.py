from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.slid import slid


def test_slid():
  """Test module slid.py by downloading
   slid.csv and testing shape of
   extracted data has 7425 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = slid(test_path)
  try:
    assert x_train.shape == (7425, 5)
  except:
    shutil.rmtree(test_path)
    raise()
