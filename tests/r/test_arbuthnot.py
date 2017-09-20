from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.arbuthnot import arbuthnot


def test_arbuthnot():
  """Test module arbuthnot.py by downloading
   arbuthnot.csv and testing shape of
   extracted data has 82 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = arbuthnot(test_path)
  try:
    assert x_train.shape == (82, 7)
  except:
    shutil.rmtree(test_path)
    raise()
