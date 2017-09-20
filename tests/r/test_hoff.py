from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.hoff import hoff


def test_hoff():
  """Test module hoff.py by downloading
   hoff.csv and testing shape of
   extracted data has 36 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = hoff(test_path)
  try:
    assert x_train.shape == (36, 5)
  except:
    shutil.rmtree(test_path)
    raise()
