from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.pilot import pilot


def test_pilot():
  """Test module pilot.py by downloading
   pilot.csv and testing shape of
   extracted data has 20 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = pilot(test_path)
  try:
    assert x_train.shape == (20, 2)
  except:
    shutil.rmtree(test_path)
    raise()
