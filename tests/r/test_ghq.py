from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ghq import ghq


def test_ghq():
  """Test module ghq.py by downloading
   ghq.csv and testing shape of
   extracted data has 22 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ghq(test_path)
  try:
    assert x_train.shape == (22, 4)
  except:
    shutil.rmtree(test_path)
    raise()
