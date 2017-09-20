from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.weight_loss import weight_loss


def test_weight_loss():
  """Test module weight_loss.py by downloading
   weight_loss.csv and testing shape of
   extracted data has 34 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = weight_loss(test_path)
  try:
    assert x_train.shape == (34, 7)
  except:
    shutil.rmtree(test_path)
    raise()
