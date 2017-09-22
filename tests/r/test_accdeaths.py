from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.accdeaths import accdeaths


def test_accdeaths():
  """Test module accdeaths.py by downloading
   accdeaths.csv and testing shape of
   extracted data has 72 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = accdeaths(test_path)
  try:
    assert x_train.shape == (72, 2)
  except:
    shutil.rmtree(test_path)
    raise()
