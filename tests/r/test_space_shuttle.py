from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.space_shuttle import space_shuttle


def test_space_shuttle():
  """Test module space_shuttle.py by downloading
   space_shuttle.csv and testing shape of
   extracted data has 24 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = space_shuttle(test_path)
  try:
    assert x_train.shape == (24, 6)
  except:
    shutil.rmtree(test_path)
    raise()
