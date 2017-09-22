from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.bacteria import bacteria


def test_bacteria():
  """Test module bacteria.py by downloading
   bacteria.csv and testing shape of
   extracted data has 220 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = bacteria(test_path)
  try:
    assert x_train.shape == (220, 6)
  except:
    shutil.rmtree(test_path)
    raise()
