from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.ome_children import ome_children


def test_ome_children():
  """Test module ome_children.py by downloading
   ome_children.csv and testing shape of
   extracted data has 1097 rows and 7 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = ome_children(test_path)
  try:
    assert x_train.shape == (1097, 7)
  except:
    shutil.rmtree(test_path)
    raise()
