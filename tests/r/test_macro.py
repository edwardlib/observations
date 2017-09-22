from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.macro import macro


def test_macro():
  """Test module macro.py by downloading
   macro.csv and testing shape of
   extracted data has 350 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = macro(test_path)
  try:
    assert x_train.shape == (350, 6)
  except:
    shutil.rmtree(test_path)
    raise()
