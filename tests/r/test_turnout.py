from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.turnout import turnout


def test_turnout():
  """Test module turnout.py by downloading
   turnout.csv and testing shape of
   extracted data has 2000 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = turnout(test_path)
  try:
    assert x_train.shape == (2000, 5)
  except:
    shutil.rmtree(test_path)
    raise()
