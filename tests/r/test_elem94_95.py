from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.elem94_95 import elem94_95


def test_elem94_95():
  """Test module elem94_95.py by downloading
   elem94_95.csv and testing shape of
   extracted data has 1848 rows and 14 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = elem94_95(test_path)
  try:
    assert x_train.shape == (1848, 14)
  except:
    shutil.rmtree(test_path)
    raise()
