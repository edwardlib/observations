from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.topo import topo


def test_topo():
  """Test module topo.py by downloading
   topo.csv and testing shape of
   extracted data has 52 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = topo(test_path)
  try:
    assert x_train.shape == (52, 3)
  except:
    shutil.rmtree(test_path)
    raise()
