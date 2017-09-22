from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.jtrain3 import jtrain3


def test_jtrain3():
  """Test module jtrain3.py by downloading
   jtrain3.csv and testing shape of
   extracted data has 2675 rows and 20 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = jtrain3(test_path)
  try:
    assert x_train.shape == (2675, 20)
  except:
    shutil.rmtree(test_path)
    raise()
