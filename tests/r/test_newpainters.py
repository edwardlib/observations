from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.newpainters import newpainters


def test_newpainters():
  """Test module newpainters.py by downloading
   newpainters.csv and testing shape of
   extracted data has 54 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = newpainters(test_path)
  try:
    assert x_train.shape == (54, 4)
  except:
    shutil.rmtree(test_path)
    raise()
