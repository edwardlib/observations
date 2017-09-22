from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.wght_loss_incentive7 import wght_loss_incentive7


def test_wght_loss_incentive7():
  """Test module wght_loss_incentive7.py by downloading
   wght_loss_incentive7.csv and testing shape of
   extracted data has 33 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = wght_loss_incentive7(test_path)
  try:
    assert x_train.shape == (33, 2)
  except:
    shutil.rmtree(test_path)
    raise()
