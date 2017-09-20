from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.voteincome import voteincome


def test_voteincome():
  """Test module voteincome.py by downloading
   voteincome.csv and testing shape of
   extracted data has 1500 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = voteincome(test_path)
  try:
    assert x_train.shape == (1500, 7)
  except:
    shutil.rmtree(test_path)
    raise()
