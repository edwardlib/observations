from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.saxony import saxony


def test_saxony():
  """Test module saxony.py by downloading
   saxony.csv and testing shape of
   extracted data has 13 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = saxony(test_path)
  try:
    assert x_train.shape == (13, 2)
  except:
    shutil.rmtree(test_path)
    raise()
