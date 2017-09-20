from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.minard_temp import minard_temp


def test_minard_temp():
  """Test module minard_temp.py by downloading
   minard_temp.csv and testing shape of
   extracted data has 9 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = minard_temp(test_path)
  try:
    assert x_train.shape == (9, 4)
  except:
    shutil.rmtree(test_path)
    raise()
