from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ezanders import ezanders


def test_ezanders():
  """Test module ezanders.py by downloading
   ezanders.csv and testing shape of
   extracted data has 108 rows and 25 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ezanders(test_path)
  try:
    assert x_train.shape == (108, 25)
  except:
    shutil.rmtree(test_path)
    raise()
