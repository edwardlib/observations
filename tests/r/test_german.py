from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.german import german


def test_german():
  """Test module german.py by downloading
   german.csv and testing shape of
   extracted data has 1000 rows and 21 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = german(test_path)
  try:
    assert x_train.shape == (1000, 21)
  except:
    shutil.rmtree(test_path)
    raise()
