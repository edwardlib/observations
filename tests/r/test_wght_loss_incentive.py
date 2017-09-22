from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.wght_loss_incentive import wght_loss_incentive


def test_wght_loss_incentive():
  """Test module wght_loss_incentive.py by downloading
   wght_loss_incentive.csv and testing shape of
   extracted data has 38 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = wght_loss_incentive(test_path)
  try:
    assert x_train.shape == (38, 3)
  except:
    shutil.rmtree(test_path)
    raise()
