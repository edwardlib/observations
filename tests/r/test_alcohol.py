from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.alcohol import alcohol


def test_alcohol():
  """Test module alcohol.py by downloading
   alcohol.csv and testing shape of
   extracted data has 9822 rows and 33 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = alcohol(test_path)
  try:
    assert x_train.shape == (9822, 33)
  except:
    shutil.rmtree(test_path)
    raise()
