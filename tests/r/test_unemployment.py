from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.unemployment import unemployment


def test_unemployment():
  """Test module unemployment.py by downloading
   unemployment.csv and testing shape of
   extracted data has 452 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = unemployment(test_path)
  try:
    assert x_train.shape == (452, 12)
  except:
    shutil.rmtree(test_path)
    raise()
