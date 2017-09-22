from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.crimtab import crimtab


def test_crimtab():
  """Test module crimtab.py by downloading
   crimtab.csv and testing shape of
   extracted data has 42 rows and 22 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = crimtab(test_path)
  try:
    assert x_train.shape == (42, 22)
  except:
    shutil.rmtree(test_path)
    raise()
