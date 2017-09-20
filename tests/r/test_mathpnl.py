from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.mathpnl import mathpnl


def test_mathpnl():
  """Test module mathpnl.py by downloading
   mathpnl.csv and testing shape of
   extracted data has 3850 rows and 52 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = mathpnl(test_path)
  try:
    assert x_train.shape == (3850, 52)
  except:
    shutil.rmtree(test_path)
    raise()
