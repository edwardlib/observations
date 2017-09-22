from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.goose_permits import goose_permits


def test_goose_permits():
  """Test module goose_permits.py by downloading
   goose_permits.csv and testing shape of
   extracted data has 11 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = goose_permits(test_path)
  try:
    assert x_train.shape == (11, 3)
  except:
    shutil.rmtree(test_path)
    raise()
