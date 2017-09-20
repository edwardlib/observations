from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.jtrain2 import jtrain2


def test_jtrain2():
  """Test module jtrain2.py by downloading
   jtrain2.csv and testing shape of
   extracted data has 445 rows and 19 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = jtrain2(test_path)
  try:
    assert x_train.shape == (445, 19)
  except:
    shutil.rmtree(test_path)
    raise()
