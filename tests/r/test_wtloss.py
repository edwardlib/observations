from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.wtloss import wtloss


def test_wtloss():
  """Test module wtloss.py by downloading
   wtloss.csv and testing shape of
   extracted data has 52 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = wtloss(test_path)
  try:
    assert x_train.shape == (52, 2)
  except:
    shutil.rmtree(test_path)
    raise()
