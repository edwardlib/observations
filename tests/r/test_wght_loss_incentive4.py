from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.wght_loss_incentive4 import wght_loss_incentive4


def test_wght_loss_incentive4():
  """Test module wght_loss_incentive4.py by downloading
   wght_loss_incentive4.csv and testing shape of
   extracted data has 36 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = wght_loss_incentive4(test_path)
  try:
    assert x_train.shape == (36, 2)
  except:
    shutil.rmtree(test_path)
    raise()
