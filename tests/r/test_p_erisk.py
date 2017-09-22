from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.p_erisk import p_erisk


def test_p_erisk():
  """Test module p_erisk.py by downloading
   p_erisk.csv and testing shape of
   extracted data has 62 rows and 6 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = p_erisk(test_path)
  try:
    assert x_train.shape == (62, 6)
  except:
    shutil.rmtree(test_path)
    raise()
