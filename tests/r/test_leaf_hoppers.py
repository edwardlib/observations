from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.leaf_hoppers import leaf_hoppers


def test_leaf_hoppers():
  """Test module leaf_hoppers.py by downloading
   leaf_hoppers.csv and testing shape of
   extracted data has 8 rows and 2 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = leaf_hoppers(test_path)
  try:
    assert x_train.shape == (8, 2)
  except:
    shutil.rmtree(test_path)
    raise()
