from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.old_maps import old_maps


def test_old_maps():
  """Test module old_maps.py by downloading
   old_maps.csv and testing shape of
   extracted data has 468 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = old_maps(test_path)
  try:
    assert x_train.shape == (468, 6)
  except:
    shutil.rmtree(test_path)
    raise()
