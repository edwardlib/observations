from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cp_sch3 import cp_sch3


def test_cp_sch3():
  """Test module cp_sch3.py by downloading
   cp_sch3.csv and testing shape of
   extracted data has 11130 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cp_sch3(test_path)
  try:
    assert x_train.shape == (11130, 3)
  except:
    shutil.rmtree(test_path)
    raise()
