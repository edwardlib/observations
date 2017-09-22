from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.shrimp import shrimp


def test_shrimp():
  """Test module shrimp.py by downloading
   shrimp.csv and testing shape of
   extracted data has 18 rows and 1 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = shrimp(test_path)
  try:
    assert x_train.shape == (18, 1)
  except:
    shutil.rmtree(test_path)
    raise()
