from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.twins import twins


def test_twins():
  """Test module twins.py by downloading
   twins.csv and testing shape of
   extracted data has 24 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = twins(test_path)
  try:
    assert x_train.shape == (24, 4)
  except:
    shutil.rmtree(test_path)
    raise()
