from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.chirot import chirot


def test_chirot():
  """Test module chirot.py by downloading
   chirot.csv and testing shape of
   extracted data has 32 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = chirot(test_path)
  try:
    assert x_train.shape == (32, 5)
  except:
    shutil.rmtree(test_path)
    raise()
