from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.mifem import mifem


def test_mifem():
  """Test module mifem.py by downloading
   mifem.csv and testing shape of
   extracted data has 1295 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = mifem(test_path)
  try:
    assert x_train.shape == (1295, 10)
  except:
    shutil.rmtree(test_path)
    raise()
