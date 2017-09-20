from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.downs_bc import downs_bc


def test_downs_bc():
  """Test module downs_bc.py by downloading
   downs_bc.csv and testing shape of
   extracted data has 30 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = downs_bc(test_path)
  try:
    assert x_train.shape == (30, 3)
  except:
    shutil.rmtree(test_path)
    raise()
