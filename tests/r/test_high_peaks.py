from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.high_peaks import high_peaks


def test_high_peaks():
  """Test module high_peaks.py by downloading
   high_peaks.csv and testing shape of
   extracted data has 46 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = high_peaks(test_path)
  try:
    assert x_train.shape == (46, 6)
  except:
    shutil.rmtree(test_path)
    raise()
