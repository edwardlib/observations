from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.intdef import intdef


def test_intdef():
  """Test module intdef.py by downloading
   intdef.csv and testing shape of
   extracted data has 56 rows and 13 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = intdef(test_path)
  try:
    assert x_train.shape == (56, 13)
  except:
    shutil.rmtree(test_path)
    raise()
