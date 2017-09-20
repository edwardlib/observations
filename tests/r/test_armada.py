from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.armada import armada


def test_armada():
  """Test module armada.py by downloading
   armada.csv and testing shape of
   extracted data has 10 rows and 11 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = armada(test_path)
  try:
    assert x_train.shape == (10, 11)
  except:
    shutil.rmtree(test_path)
    raise()
