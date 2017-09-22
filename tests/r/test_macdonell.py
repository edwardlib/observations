from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.macdonell import macdonell


def test_macdonell():
  """Test module macdonell.py by downloading
   macdonell.csv and testing shape of
   extracted data has 924 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = macdonell(test_path)
  try:
    assert x_train.shape == (924, 3)
  except:
    shutil.rmtree(test_path)
    raise()
