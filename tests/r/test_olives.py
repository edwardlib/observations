from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.olives import olives


def test_olives():
  """Test module olives.py by downloading
   olives.csv and testing shape of
   extracted data has 18 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = olives(test_path)
  try:
    assert x_train.shape == (18, 7)
  except:
    shutil.rmtree(test_path)
    raise()
