from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.vaso import vaso


def test_vaso():
  """Test module vaso.py by downloading
   vaso.csv and testing shape of
   extracted data has 39 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = vaso(test_path)
  try:
    assert x_train.shape == (39, 3)
  except:
    shutil.rmtree(test_path)
    raise()
