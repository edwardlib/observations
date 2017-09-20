from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.suicide import suicide


def test_suicide():
  """Test module suicide.py by downloading
   suicide.csv and testing shape of
   extracted data has 306 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = suicide(test_path)
  try:
    assert x_train.shape == (306, 6)
  except:
    shutil.rmtree(test_path)
    raise()
