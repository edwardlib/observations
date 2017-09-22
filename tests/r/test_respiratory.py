from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.respiratory import respiratory


def test_respiratory():
  """Test module respiratory.py by downloading
   respiratory.csv and testing shape of
   extracted data has 444 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = respiratory(test_path)
  try:
    assert x_train.shape == (444, 8)
  except:
    shutil.rmtree(test_path)
    raise()
