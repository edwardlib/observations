from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.badhealth import badhealth


def test_badhealth():
  """Test module badhealth.py by downloading
   badhealth.csv and testing shape of
   extracted data has 1127 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = badhealth(test_path)
  try:
    assert x_train.shape == (1127, 3)
  except:
    shutil.rmtree(test_path)
    raise()
