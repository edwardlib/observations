from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.hurric_named import hurric_named


def test_hurric_named():
  """Test module hurric_named.py by downloading
   hurric_named.csv and testing shape of
   extracted data has 94 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = hurric_named(test_path)
  try:
    assert x_train.shape == (94, 12)
  except:
    shutil.rmtree(test_path)
    raise()
