from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.indian_irish import indian_irish


def test_indian_irish():
  """Test module indian_irish.py by downloading
   indian_irish.csv and testing shape of
   extracted data has 18 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = indian_irish(test_path)
  try:
    assert x_train.shape == (18, 4)
  except:
    shutil.rmtree(test_path)
    raise()
