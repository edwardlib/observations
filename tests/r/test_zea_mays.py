from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.zea_mays import zea_mays


def test_zea_mays():
  """Test module zea_mays.py by downloading
   zea_mays.csv and testing shape of
   extracted data has 15 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = zea_mays(test_path)
  try:
    assert x_train.shape == (15, 5)
  except:
    shutil.rmtree(test_path)
    raise()
