from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.australian_elections import australian_elections


def test_australian_elections():
  """Test module australian_elections.py by downloading
   australian_elections.csv and testing shape of
   extracted data has 24 rows and 19 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = australian_elections(test_path)
  try:
    assert x_train.shape == (24, 19)
  except:
    shutil.rmtree(test_path)
    raise()
