from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.voucher import voucher


def test_voucher():
  """Test module voucher.py by downloading
   voucher.csv and testing shape of
   extracted data has 990 rows and 19 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = voucher(test_path)
  try:
    assert x_train.shape == (990, 19)
  except:
    shutil.rmtree(test_path)
    raise()
