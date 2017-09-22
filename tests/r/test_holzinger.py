from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.holzinger import holzinger


def test_holzinger():
  """Test module holzinger.py by downloading
   holzinger.csv and testing shape of
   extracted data has 14 rows and 14 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = holzinger(test_path)
  try:
    assert x_train.shape == (14, 14)
  except:
    shutil.rmtree(test_path)
    raise()
