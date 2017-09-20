from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.metal import metal


def test_metal():
  """Test module metal.py by downloading
   metal.csv and testing shape of
   extracted data has 27 rows and 3 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = metal(test_path)
  try:
    assert x_train.shape == (27, 3)
  except:
    shutil.rmtree(test_path)
    raise()
