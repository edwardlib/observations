from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.infert import infert


def test_infert():
  """Test module infert.py by downloading
   infert.csv and testing shape of
   extracted data has 248 rows and 8 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = infert(test_path)
  try:
    assert x_train.shape == (248, 8)
  except:
    shutil.rmtree(test_path)
    raise()
