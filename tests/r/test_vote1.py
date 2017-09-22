from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.vote1 import vote1


def test_vote1():
  """Test module vote1.py by downloading
   vote1.csv and testing shape of
   extracted data has 173 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = vote1(test_path)
  try:
    assert x_train.shape == (173, 10)
  except:
    shutil.rmtree(test_path)
    raise()
