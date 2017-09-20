from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.absentee import absentee


def test_absentee():
  """Test module absentee.py by downloading
   absentee.csv and testing shape of
   extracted data has 22 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = absentee(test_path)
  try:
    assert x_train.shape == (22, 8)
  except:
    shutil.rmtree(test_path)
    raise()
