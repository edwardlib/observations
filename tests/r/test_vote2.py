from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.vote2 import vote2


def test_vote2():
  """Test module vote2.py by downloading
   vote2.csv and testing shape of
   extracted data has 186 rows and 26 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = vote2(test_path)
  try:
    assert x_train.shape == (186, 26)
  except:
    shutil.rmtree(test_path)
    raise()
