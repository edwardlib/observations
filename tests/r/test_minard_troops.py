from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.minard_troops import minard_troops


def test_minard_troops():
  """Test module minard_troops.py by downloading
   minard_troops.csv and testing shape of
   extracted data has 51 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = minard_troops(test_path)
  try:
    assert x_train.shape == (51, 5)
  except:
    shutil.rmtree(test_path)
    raise()
