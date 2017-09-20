from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.grocery import grocery


def test_grocery():
  """Test module grocery.py by downloading
   grocery.csv and testing shape of
   extracted data has 36 rows and 5 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = grocery(test_path)
  try:
    assert x_train.shape == (36, 5)
  except:
    shutil.rmtree(test_path)
    raise()
