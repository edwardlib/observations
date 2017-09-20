from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.whiteside import whiteside


def test_whiteside():
  """Test module whiteside.py by downloading
   whiteside.csv and testing shape of
   extracted data has 56 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = whiteside(test_path)
  try:
    assert x_train.shape == (56, 3)
  except:
    shutil.rmtree(test_path)
    raise()
