from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.fishing import fishing


def test_fishing():
  """Test module fishing.py by downloading
   fishing.csv and testing shape of
   extracted data has 147 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = fishing(test_path)
  try:
    assert x_train.shape == (147, 7)
  except:
    shutil.rmtree(test_path)
    raise()
