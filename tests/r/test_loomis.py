from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.loomis import loomis


def test_loomis():
  """Test module loomis.py by downloading
   loomis.csv and testing shape of
   extracted data has 410 rows and 11 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = loomis(test_path)
  try:
    assert x_train.shape == (410, 11)
  except:
    shutil.rmtree(test_path)
    raise()
