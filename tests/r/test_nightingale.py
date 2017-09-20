from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.nightingale import nightingale


def test_nightingale():
  """Test module nightingale.py by downloading
   nightingale.csv and testing shape of
   extracted data has 24 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = nightingale(test_path)
  try:
    assert x_train.shape == (24, 10)
  except:
    shutil.rmtree(test_path)
    raise()
