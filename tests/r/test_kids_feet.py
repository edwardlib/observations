from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.kids_feet import kids_feet


def test_kids_feet():
  """Test module kids_feet.py by downloading
   kids_feet.csv and testing shape of
   extracted data has 39 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = kids_feet(test_path)
  try:
    assert x_train.shape == (39, 8)
  except:
    shutil.rmtree(test_path)
    raise()
