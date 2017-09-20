from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.galaxies import galaxies


def test_galaxies():
  """Test module galaxies.py by downloading
   galaxies.csv and testing shape of
   extracted data has 82 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = galaxies(test_path)
  try:
    assert x_train.shape == (82, 1)
  except:
    shutil.rmtree(test_path)
    raise()
