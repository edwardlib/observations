from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.migration import migration


def test_migration():
  """Test module migration.py by downloading
   migration.csv and testing shape of
   extracted data has 90 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = migration(test_path)
  try:
    assert x_train.shape == (90, 8)
  except:
    shutil.rmtree(test_path)
    raise()
