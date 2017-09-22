from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.nodal import nodal


def test_nodal():
  """Test module nodal.py by downloading
   nodal.csv and testing shape of
   extracted data has 53 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = nodal(test_path)
  try:
    assert x_train.shape == (53, 7)
  except:
    shutil.rmtree(test_path)
    raise()
