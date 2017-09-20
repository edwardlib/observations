from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.gleser import gleser


def test_gleser():
  """Test module gleser.py by downloading
   gleser.csv and testing shape of
   extracted data has 12 rows and 12 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = gleser(test_path)
  try:
    assert x_train.shape == (12, 12)
  except:
    shutil.rmtree(test_path)
    raise()
