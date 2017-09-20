from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.penicillin import penicillin


def test_penicillin():
  """Test module penicillin.py by downloading
   penicillin.csv and testing shape of
   extracted data has 144 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = penicillin(test_path)
  try:
    assert x_train.shape == (144, 3)
  except:
    shutil.rmtree(test_path)
    raise()
