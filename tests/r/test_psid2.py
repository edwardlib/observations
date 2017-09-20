from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.psid2 import psid2


def test_psid2():
  """Test module psid2.py by downloading
   psid2.csv and testing shape of
   extracted data has 253 rows and 10 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = psid2(test_path)
  try:
    assert x_train.shape == (253, 10)
  except:
    shutil.rmtree(test_path)
    raise()
