from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bee_stings import bee_stings


def test_bee_stings():
  """Test module bee_stings.py by downloading
   bee_stings.csv and testing shape of
   extracted data has 18 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bee_stings(test_path)
  try:
    assert x_train.shape == (18, 3)
  except:
    shutil.rmtree(test_path)
    raise()
